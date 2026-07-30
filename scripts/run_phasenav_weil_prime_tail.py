#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
from secret_of_a_half.phasenav_weil_hermite_core import HermiteLadderProgram
from secret_of_a_half.phasenav_weil_prime_tail import PrimeTailProgram, run_prime_tail_certificate

ROOT=Path(__file__).resolve().parents[1]

def main()->int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--tail-program',type=Path,default=ROOT/'construction/phasenav/secret_of_half_weil_prime_tail_certificate.pnv')
    parser.add_argument('--hermite-program',type=Path,default=ROOT/'construction/phasenav/secret_of_half_weil_hermite_ladder.pnv')
    parser.add_argument('--output',type=Path,default=ROOT/'data/processed/phasenav_weil_prime_tail_certificate.json')
    args=parser.parse_args()
    receipt=run_prime_tail_certificate(PrimeTailProgram.load(args.tail_program),HermiteLadderProgram.load(args.hermite_program))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({
        'integral_identity_pass':receipt['integral_identity_pass'],
        'all_operator_norm_targets_pass':receipt['all_operator_norm_targets_pass'],
        'all_shell_checks_pass':receipt['all_shell_checks_pass'],
        'n6_operator_norm_bound':receipt['sections'][-1]['operator_norm_bound'],
        'output':str(args.output),
    },indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
