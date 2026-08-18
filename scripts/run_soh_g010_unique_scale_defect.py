#!/usr/bin/env python3
from __future__ import annotations

import json
import mpmath as mp
from pathlib import Path

from secret_of_a_half.scale_defect import scale_defect, scale_defect_crossing

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports' / 'SOH_G010_UNIQUE_SCALE_DEFECT_RECEIPT_V1.json'


def main() -> None:
    mp.mp.dps = 60
    rows = []
    for a in [2, 3, 32]:
        c = mp.mpf(1) / mp.sqrt(a)
        d0 = scale_defect(c, a)
        left = scale_defect(c / 2, a)
        right = scale_defect(c * 2, a)
        if abs(d0) > mp.mpf('1e-45') or not (left < 0 < right):
            raise RuntimeError(f'scale-defect crossing verification failed for a={a}')
        rows.append({'a': a, 'crossing': mp.nstr(c, 30), 'left_negative': True, 'right_positive': True})
    payload = {
        'certificate': 'SOH_G010_UNIQUE_SCALE_DEFECT_RECEIPT_V1',
        'status': 'THEOREM_NUMERIC_REGRESSION_PASS',
        'rows': rows,
        'claims': {'unique_positive_crossing_proved_analytically': True, 'complex_zero_location_proved': False, 'rh_proved': False},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
