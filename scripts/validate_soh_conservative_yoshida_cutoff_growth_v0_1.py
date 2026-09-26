#!/usr/bin/env python3
"""Log-domain regression for the current c=2 Yoshida high-mode cutoff asymptotic."""
from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80


def log_required_cutoff(a: mp.mpf, mu=mp.mpf(1), margin=mp.mpf(1)) -> mp.mpf:
    a1 = a + 1 / a
    c1 = mp.mpf(5) / 6
    c2 = mp.expm1(4 * a1) / (4 * a1)
    p = c1 * c2
    C = 3 * p + mp.pi * mu + margin

    log_t0 = mp.log(2 * mp.sqrt(mp.pi)) + C + 1

    upper_coeff = mp.sqrt(2) / 6 - mp.mpf(1) / 8
    # rmax=sqrt(1/16+t0^2/4), evaluated stably in log-domain.
    log_rmax = (
        log_t0
        - mp.log(2)
        + mp.log1p(mp.mpf("0.25") * mp.e ** (-2 * log_t0)) / 2
    )
    C0 = log_rmax + 16 * upper_coeff - mp.log(mp.pi) / 2

    # B=(8a/pi^2)*(t+a t^2+a^2 t^3/3), again in log-domain.
    log_B = (
        mp.log(8 * a / mp.pi**2)
        + 3 * log_t0
        + mp.log(
            a * a / 3
            + a * mp.e ** (-log_t0)
            + mp.e ** (-2 * log_t0)
        )
    )

    denominator = p + margin
    return mp.log(C + C0) + log_B - mp.log(denominator)


def asymptotic_loglog(a: mp.mpf) -> mp.mpf:
    return 4 * a - mp.log(a) + mp.log(mp.mpf(15) / 8)


def main() -> None:
    rows = []
    for a0 in [2, 3, 4, 5, 6, 8, 10]:
        a = mp.mpf(a0)
        logN = log_required_cutoff(a)
        loglog = mp.log(logN)
        model = asymptotic_loglog(a)
        residual = loglog - model
        rows.append((a0, loglog, model, residual))

    # The chosen a1=a+1/a leaves a leading finite-a correction ~4/a.
    scaled = [a * residual for a, _, _, residual in rows[-4:]]
    for x in scaled:
        assert mp.isfinite(x)
        assert x > 0
        assert x < 5

    # Residual decreases across this asymptotic regression window.
    residuals = [row[3] for row in rows]
    assert all(residuals[i+1] < residuals[i] for i in range(len(residuals)-1))

    print("SOH_CONSERVATIVE_YOSHIDA_HIGH_MODE_CUTOFF_GROWTH_V0_1: PASS")
    for a, loglog, model, residual in rows:
        print(
            "a=", a,
            " loglogN=", mp.nstr(loglog, 16),
            " model=", mp.nstr(model, 16),
            " residual=", mp.nstr(residual, 12),
        )
    print("MINIMAL_CUTOFF_CLAIM=false")
    print("STATUS=CURRENT_CERTIFICATE_ASYMPTOTIC")


if __name__ == "__main__":
    main()
