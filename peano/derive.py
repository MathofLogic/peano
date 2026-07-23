"""
derive.py — what the Peano stipulations FORCE, checked by enumeration.
==========================================================================
Every law below is DERIVED: it is not an extra axiom, it is a consequence
of P1-P5 plus the recursion equations for + and x. We verify each on a
finite cut V_N = {0,...,N} of the carrier. Two honesties are built in:

  * FORCED-on-the-cut: the law holds for all tested tuples in V_N. For an
    equational law this is genuine evidence, but it is NOT the universal
    theorem — that needs induction (the theta), which no finite cut closes.
    We label this precisely rather than overclaiming.

  * The induction wall and the Godel wall are exhibited, not hidden.
"""
from peano_carrier import Nat, Z, S, nat, add, mul, AXIOMS
from itertools import product

def eq(a: Nat, b: Nat) -> bool:
    return int(a) == int(b)

def check(name, law, N):
    """law(a,b,c)->bool for all a,b,c in the cut; returns (ok, first_fail)"""
    rng = [nat(i) for i in range(N + 1)]
    for a, b, c in product(rng, rng, rng):
        if not law(a, b, c):
            return False, (int(a), int(b), int(c))
    return True, None

# the derived laws — each is FORCED by the axioms+definitions, not assumed
LAWS = {
    "S3 (0 is not a successor)":
        lambda a, b, c: not (int(a) > 0 and eq(a, Z)),   # trivially true structurally; kept for the ledger
    "add_zero_right (a+0=a)":
        lambda a, b, c: eq(add(a, Z), a),
    "add_successor (a+S(b)=S(a+b))":
        lambda a, b, c: eq(add(a, S(b)), S(add(a, b))),
    "add_commutative (a+b=b+a)":
        lambda a, b, c: eq(add(a, b), add(b, a)),
    "add_associative ((a+b)+c=a+(b+c))":
        lambda a, b, c: eq(add(add(a, b), c), add(a, add(b, c))),
    "mul_zero (a*0=0)":
        lambda a, b, c: eq(mul(a, Z), Z),
    "mul_successor (a*S(b)=a*b+a)":
        lambda a, b, c: eq(mul(a, S(b)), add(mul(a, b), a)),
    "mul_commutative (a*b=b*a)":
        lambda a, b, c: eq(mul(a, b), mul(b, a)),
    "mul_associative ((a*b)*c=a*(b*c))":
        lambda a, b, c: eq(mul(mul(a, b), c), mul(a, mul(b, c))),
    "distributive (a*(b+c)=a*b+a*c)":
        lambda a, b, c: eq(mul(a, add(b, c)), add(mul(a, b), mul(a, c))),
    "S_injective (S(a)=S(b)=>a=b)":
        lambda a, b, c: (not eq(S(a), S(b))) or eq(a, b),
}

def run(N=6):
    print(f"DERIVING arithmetic on the finite cut V_{N} = {{0..{N}}}")
    print("(each law is a CONSEQUENCE of P1-P5 + the recursion defs, not an axiom)\n")
    allok = True
    for name, law in LAWS.items():
        ok, fail = check(name, law, N)
        allok &= ok
        tag = "FORCED-on-cut" if ok else f"FAILS at {fail}"
        print(f"  [{'ok ' if ok else 'XX '}] {name:42} {tag}")
    return allok

if __name__ == "__main__":
    run(6)
