#!/usr/bin/env python3
"""
SOH-HYB-007 — Jensen–HTRI angle / 3-point Gram verifier

Evidential status:
    FINITE_DIAGNOSTIC_NOT_PROOF

The exact analytic reduction used by this verifier is

    rho_eta(u)   = J_eta(u) / J_eta(0)
    theta_eta(u) = arccos(rho_eta(u))

and for points {0,a,b}

    det G3
      = 1 + 2 rho(a)rho(b)rho(|a-b|)
          - rho(a)^2-rho(b)^2-rho(|a-b|)^2

      = 4 sin(s) sin(s-alpha) sin(s-beta) sin(s-gamma),

where alpha=theta(a), beta=theta(b), gamma=theta(|a-b|)
and s=(alpha+beta+gamma)/2.

Thus concavity + monotonicity of theta_eta on R_+ is a sufficient
condition for every 3-point translation-invariant Gram matrix to be PSD.

Qiskit is NOT needed for this theorem; see SOH-HYB-006 for the
independent finite Hadamard-test verifier.
"""

from __future__ import annotations
import argparse
import math
import numpy as np


def phi_positive(t, nmax=40):
    t = np.asarray(t, dtype=np.float64)
    x = np.abs(t).ravel()
    e2 = np.exp(2.0*x)
    out = np.zeros_like(x)
    for n in range(1, nmax+1):
        a = np.pi*n*n
        out += 4*a*np.exp(2.5*x)*(2*a*e2-3)*np.exp(-a*e2)
    return out.reshape(t.shape)


def K_even(t):
    return 0.5*phi_positive(t)


class JensenInternal:
    def __init__(self, eta, quad_order=700, rmax=3.5):
        if not (abs(eta) < 0.5):
            raise ValueError("|eta| must be < 1/2")
        self.eta = float(eta)
        z,w = np.polynomial.legendre.leggauss(int(quad_order))
        self.r = rmax*z
        self.w = rmax*w
        self.pref = self.w*(self.r**2)*np.cosh(2*self.eta*self.r)
        self.j0 = self.J(0.0)

    def J(self, u):
        r=self.r
        return float(np.sum(self.pref*K_even(u+r)*K_even(u-r)))

    def rho(self,u):
        return self.J(abs(float(u)))/self.j0

    def theta(self,u):
        r=min(1.0,max(-1.0,self.rho(u)))
        return math.acos(r)

    def gram3_det(self,a,b):
        x=self.rho(a)
        y=self.rho(b)
        z=self.rho(abs(a-b))
        return 1+2*x*y*z-x*x-y*y-z*z

    def angle_heron(self,a,b):
        A=self.theta(a)
        B=self.theta(b)
        C=self.theta(abs(a-b))
        s=(A+B+C)/2
        return 4*math.sin(s)*math.sin(s-A)*math.sin(s-B)*math.sin(s-C)

    def triangle_slacks(self,a,b):
        A=self.theta(a)
        B=self.theta(b)
        C=self.theta(abs(a-b))
        return (
            A+B-C,
            A+C-B,
            B+C-A,
        )


def finite_angle_margin(model, umax=1.8, n=721):
    u=np.linspace(0.0,umax,n)
    j=np.array([model.J(float(x)) for x in u])
    rho=j/j[0]
    theta=np.arccos(np.clip(rho,-1,1))
    h=u[1]-u[0]
    d1=(theta[2:]-theta[:-2])/(2*h)
    d2=(theta[2:]-2*theta[1:-1]+theta[:-2])/(h*h)
    return {
        "min_theta_prime": float(np.min(d1)),
        "max_theta_second": float(np.max(d2[8:])),
        "min_theta_second": float(np.min(d2[8:])),
    }


def random_triples(model, seed=20260821, count=2000, span=1.5):
    rng=np.random.default_rng(seed)
    worst=math.inf
    worst_data=None
    identity_res=0.0
    triangle_min=math.inf
    for _ in range(count):
        a,b=np.sort(rng.uniform(0,span,2))
        d=model.gram3_det(a,b)
        h=model.angle_heron(a,b)
        identity_res=max(identity_res,abs(d-h))
        sl=min(model.triangle_slacks(a,b))
        triangle_min=min(triangle_min,sl)
        if d<worst:
            worst=d
            worst_data=(float(a),float(b))
    return {
        "count": count,
        "min_det_G3": worst,
        "worst_pair": worst_data,
        "min_triangle_slack": triangle_min,
        "max_det_vs_angle_identity_residual": identity_res,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--eta",type=float,default=0.49)
    ap.add_argument("--triples",type=int,default=2000)
    ap.add_argument("--span",type=float,default=1.5)
    args=ap.parse_args()

    m=JensenInternal(args.eta)
    am=finite_angle_margin(m)
    rt=random_triples(m,count=args.triples,span=args.span)

    print("SOH-HYB-007")
    print("status=FINITE_DIAGNOSTIC_NOT_PROOF")
    print(f"eta={args.eta}")
    for k,v in am.items():
        print(f"{k}={v:.17g}")
    for k,v in rt.items():
        print(f"{k}={v}")

if __name__=="__main__":
    main()
