from fractions import Fraction

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))

def add(a,b):
    return tuple(tuple(x+y for x,y in zip(ra,rb)) for ra,rb in zip(a,b))

def sub(a,b):
    return tuple(tuple(x-y for x,y in zip(ra,rb)) for ra,rb in zip(a,b))

def scale(a,s):
    return tuple(tuple(s*x for x in row) for row in a)

def validate():
    I=tuple(tuple(Fraction(int(i==j)) for j in range(6)) for i in range(6))
    star=[[Fraction(0) for _ in range(6)] for _ in range(6)]
    for i in range(3):
        star[i][i+3]=Fraction(1)
        star[i+3][i]=Fraction(1)
    star=tuple(tuple(r) for r in star)

    D=tuple(
        tuple(
            Fraction(-1 if i==j and i<3 else 1 if i==j else 0)
            for j in range(6)
        )
        for i in range(6)
    )

    Pp=scale(add(I,star),Fraction(1,2))
    Pm=scale(sub(I,star),Fraction(1,2))
    zero=tuple(tuple(Fraction(0) for _ in range(6)) for _ in range(6))

    checks={
        "star_square_identity": matmul(star,star)==I,
        "pplus_idempotent": matmul(Pp,Pp)==Pp,
        "pminus_idempotent": matmul(Pm,Pm)==Pm,
        "projectors_orthogonal": matmul(Pp,Pm)==zero,
        "projectors_sum_identity": add(Pp,Pm)==I,
        "rank_trace_three_each": sum(Pp[i][i] for i in range(6))==3 and sum(Pm[i][i] for i in range(6))==3,
        "parity_hodge_anticommutation": matmul(matmul(D,star),D)==scale(star,Fraction(-1)),
        "parity_swaps_plus_to_minus": matmul(matmul(D,Pp),D)==Pm,
        "parity_swaps_minus_to_plus": matmul(matmul(D,Pm),D)==Pp,
    }
    return {
        "schema":"SOH_STELLA_PARITY_CHIRAL_SWAP_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "rh_claim":False,
        "candidate_only":True,
    }

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True))
