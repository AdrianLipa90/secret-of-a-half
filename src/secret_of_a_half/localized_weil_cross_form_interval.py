"""Interval certificate for the localized Weil cross-form rank witness.

The compact cross-convolution is exact.  The regularization integral is
expanded into a convergent geometric series.  Its tail is split into:
1. a rational tail accelerated by a finite 1/k expansion with explicit
   integral-test enclosures for the p-series;
2. an exponentially small tail enclosed directly.

All finite arithmetic uses mpmath.iv outward interval arithmetic.

This is a machine-assisted interval certificate.  Its trust base includes
Python, mpmath.iv, and the algebra implemented here; it is not a formally
verified proof assistant artifact.
"""
from __future__ import annotations

import mpmath as mp


iv=mp.iv
iv.dps=max(iv.dps,50)


def _c(re,im):
    return iv.mpc(iv.mpf(str(re)),iv.mpf(str(im)))


def _conj(z):
    return iv.mpc(z.real,-z.imag)


def _atanh(x):
    return iv.log((1+x)/(1-x))/2


def _E(r,T):
    return (iv.exp(r*T)-1)/r


def _prime_power_pairs(N: int):
    if N<2:
        return []
    sieve=[True]*(N+1)
    sieve[0]=sieve[1]=False
    p=2
    while p*p<=N:
        if sieve[p]:
            for k in range(p*p,N+1,p):
                sieve[k]=False
        p+=1
    out=[]
    for p in range(2,N+1):
        if not sieve[p]:
            continue
        q=p
        while q<=N:
            out.append((q,p))
            if q>N//p:
                break
            q*=p
    out.sort()
    return out


def _coefficients(a,z,w):
    alpha=1j*(_conj(w)-z)
    c1=iv.exp(alpha*a)/alpha
    c2=-iv.exp(-alpha*a)/alpha
    lambdas=[
        -1j*_conj(w),
        -1j*z,
        1j*z,
        1j*_conj(w),
    ]
    return c1,c2,lambdas,[c1,c2,c1,c2]


def _cross_at_point(t,a,z,w):
    tt=iv.mpf(str(t))
    c1,c2,lambdas,_=_coefficients(a,z,w)
    if t>=0:
        return c1*iv.exp(lambdas[0]*tt)+c2*iv.exp(lambdas[1]*tt)
    u=-tt
    return c1*iv.exp(lambdas[2]*u)+c2*iv.exp(lambdas[3]*u)


def _p_series_interval(K: int,p: int):
    Kiv=iv.mpf(K)
    lower=Kiv**(1-p)/(p-1)
    upper=lower+Kiv**(-p)
    return iv.mpf([lower.a,upper.b])


def _add_symmetric_radius(z,positive_radius):
    r=iv.mpf([-positive_radius.b,positive_radius.b])
    return iv.mpc(z.real+r,z.imag+r)


def _regularization_J(s,T,K: int=500,m: int=4):
    """Enclose J_T(s)=int_0^T (e^-st-e^-t)/(1-e^-2t) dt."""
    total=iv.mpc(0)

    for k in range(K):
        a=s+2*k
        b=1+2*k
        total += (1-iv.exp(-a*T))/a - (1-iv.exp(-b*T))/b

    # Accelerated rational tail.
    for j in range(1,m):
        coeff=(-1)**j*(s**j-1)/(2**(j+1))
        total += coeff*_p_series_interval(K,j+1)

    M=abs(s)
    p_tail_upper=iv.mpf(K)**(-m)/m + iv.mpf(K)**(-(m+1))
    rational_radius=(
        M**m/(1-M/(2*K))
        +1/(1-iv.mpf(1)/(2*K))
    )/(2**(m+1))*p_tail_upper

    # Exponentially small omitted terms.
    q=iv.exp(-2*T)
    exponential_radius=(
        iv.exp(-s.real*T)*q**K/((2*K-M)*(1-q))
        +iv.exp(-T)*q**K/((1+2*K)*(1-q))
    )

    return _add_symmetric_radius(
        total,
        rational_radius+exponential_radius,
    )


def localized_weil_cross_form_interval(
    a,
    z,
    w,
    *,
    K: int=500,
    tail_order: int=4,
    max_support: int=2_000_000,
):
    """Interval enclosure of Q_W^a(v_z,v_w) for point complex parameters."""
    a_text=str(a)
    aa=iv.mpf(a_text)
    if not (mp.mpf(a_text)>0):
        raise ValueError("a must be positive")
    T=2*aa

    zz=_c(z[0],z[1])
    ww=_c(w[0],w[1])
    c1,c2,lambdas,coeffs=_coefficients(aa,zz,ww)
    f0=c1+c2

    half=iv.mpf("0.5")
    elementary=iv.mpc(0)
    for c,lam in zip(coeffs,lambdas):
        elementary += c*(_E(lam+half,T)+_E(lam-half,T))

    cutoff=int(mp.floor(mp.e**(2*mp.mpf(a_text))))
    if cutoff>max_support:
        raise ValueError(
            f"prime support exp(2a)={cutoff} exceeds max_support={max_support}"
        )

    prime=iv.mpc(0)
    for n,p in _prime_power_pairs(cutoff):
        ln=mp.log(n)
        prime -= iv.log(iv.mpf(p))/iv.sqrt(iv.mpf(n))*(
            _cross_at_point(ln,aa,zz,ww)
            +_cross_at_point(-ln,aa,zz,ww)
        )

    constant=-(iv.log(4*iv.pi)+iv.euler)*f0

    regularization=iv.mpc(0)
    for c,lam in zip(coeffs,lambdas):
        regularization += c*_regularization_J(
            half-lam,
            T,
            K=K,
            m=tail_order,
        )

    regularization += -2*f0*_atanh(iv.exp(-T))

    return elementary+prime+constant-regularization


def displacement_determinant_interval(
    a,
    points,
    *,
    K: int=500,
    tail_order: int=4,
):
    pts=[(str(x),str(y)) for x,y in points]
    q=[
        [
            localized_weil_cross_form_interval(
                a,pts[j],pts[k],K=K,tail_order=tail_order
            )
            for k in range(3)
        ]
        for j in range(3)
    ]

    M=[[None]*3 for _ in range(3)]
    for j,(xr,xi) in enumerate(pts):
        z=_c(xr,xi)
        for k,(yr,yi) in enumerate(pts):
            w=_c(yr,yi)
            M[j][k]=2j*(_conj(w)-z)*q[j][k]

    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


def interval_excludes_zero(z) -> bool:
    real_positive=z.real.a>0
    real_negative=z.real.b<0
    imag_positive=z.imag.a>0
    imag_negative=z.imag.b<0
    return bool(real_positive or real_negative or imag_positive or imag_negative)
