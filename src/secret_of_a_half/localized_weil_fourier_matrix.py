"""Source-faithful localized Fourier Galerkin matrix for Suzuki's Weil form.

The normalized Fourier basis on [-a,a] is
    e_n(x) = (2a)^(-1/2) exp(pi i n x / a).

With the localized exponential convention
    v_z(x)=exp(-i z x) 1_[-a,a](x),
we have
    e_n = (2a)^(-1/2) v_{-pi n/a}.

Therefore
    A_nm(a) = Q_W^a(e_n,e_m)
            = localized_weil_cross_form(a,z_n,z_m)/(2a).

This module is numerical/high-precision, not interval certified.  It is the
localized arithmetic Galerkin matrix that was intentionally kept separate from
the global Hermite diagnostic.
"""
from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .localized_weil_cross_form import localized_weil_cross_form


mp.mp.dps=max(mp.mp.dps,80)


@dataclass(frozen=True)
class FourierBlockIndex:
    low: tuple[int,...]
    high: tuple[int,...]


def fourier_spectral_parameter(n: int,a):
    aa=mp.mpf(a)
    if aa<=0:
        raise ValueError("a must be positive")
    return -mp.pi*int(n)/aa


def localized_fourier_entry(a,n: int,m: int,**kwargs):
    aa=mp.mpf(a)
    zn=fourier_spectral_parameter(n,aa)
    zm=fourier_spectral_parameter(m,aa)
    return localized_weil_cross_form(
        aa,zn,zm,**kwargs
    )/(2*aa)


def localized_fourier_matrix(a,N: int,**kwargs):
    if N<0:
        raise ValueError("N must be non-negative")
    modes=tuple(range(-N,N+1))
    M=mp.matrix(len(modes))
    for i,n in enumerate(modes):
        for j,m in enumerate(modes):
            M[i,j]=localized_fourier_entry(a,n,m,**kwargs)
    return modes,M


def low_high_blocks(a,N_low: int,N_max: int,**kwargs):
    if N_low<0 or N_max<N_low:
        raise ValueError("require 0 <= N_low <= N_max")

    modes,M=localized_fourier_matrix(a,N_max,**kwargs)
    low_idx=[i for i,n in enumerate(modes) if abs(n)<=N_low]
    high_idx=[i for i,n in enumerate(modes) if abs(n)>N_low]

    def sub(rows,cols):
        out=mp.matrix(len(rows),len(cols))
        for i,r in enumerate(rows):
            for j,c in enumerate(cols):
                out[i,j]=M[r,c]
        return out

    return {
        "modes":modes,
        "index":FourierBlockIndex(
            low=tuple(modes[i] for i in low_idx),
            high=tuple(modes[i] for i in high_idx),
        ),
        "A_LL":sub(low_idx,low_idx),
        "B":sub(low_idx,high_idx),
        "A_HH":sub(high_idx,high_idx),
        "full":M,
    }


def hermitian_residual(M):
    rows,cols=M.rows,M.cols
    if rows!=cols:
        raise ValueError("square matrix required")
    return max(
        abs(M[i,j]-mp.conj(M[j,i]))
        for i in range(rows)
        for j in range(cols)
    )


def parity_residual(modes,M):
    pos={n:i for i,n in enumerate(modes)}
    return max(
        abs(M[pos[-n],pos[-m]]-M[pos[n],pos[m]])
        for n in modes
        for m in modes
    )
