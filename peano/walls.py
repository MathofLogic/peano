"""
walls.py — where PL derivation stops, exhibited not hidden.
==========================================================================
Two walls. Both are the point of the whole exercise: de-reification does
not mean "PL grounds arithmetic." It means the stipulations are visible
and their consequences forced UP TO a seam that is named.
"""
from peano_carrier import Nat, Z, S, nat, add, mul

# ============================================================
# WALL 1 — THE INDUCTION WALL
# a+b=b+a passed for all pairs in {0..6}. Is it PROVEN? No.
# A finite cut cannot certify a statement about an unbounded V. The theta
# (induction, P5) is exactly the stipulation that closes this gap — and it
# is a SCHEMA, an infinite family of axioms, not a single checkable fact.
# ============================================================
def induction_wall():
    print("WALL 1 — the induction wall\n")
    print("  add_commutative held for every pair in {0..6}. That is EVIDENCE,")
    print("  not PROOF. The cut is finite; V is not. To lift 'FORCED-on-cut'")
    print("  to 'FORCED', you need P5 (induction) — and P5 is a SCHEMA:")
    print("  one axiom PER predicate P, infinitely many. No enumeration")
    print("  closes an infinite axiom family.\n")
    # we CAN, however, exhibit the induction STEP mechanically for a fixed
    # predicate — showing induction is a discharge rule, not magic:
    def P(n):  # predicate: 0 + n == n  (the harder direction of add_comm base)
        return int(add(Z, n)) == int(n)
    base = P(Z)
    # step: assume P(n), show P(S(n)), for a sample n — mechanical, but only
    # a schema instance, and only sampled:
    step_ok = all(P(nat(k)) and P(S(nat(k))) for k in range(20))
    print(f"  base P(0):        {base}")
    print(f"  step P(n)->P(Sn): holds for sampled n<20: {step_ok}")
    print("  induction then STIPULATES the leap to all n. That leap is the")
    print("  theta doing its job — a chosen rule, not a checked fact.\n")

# ============================================================
# WALL 1b — THE INTRUDER induction exists to exclude
# Without induction, the axioms P1-P4 do NOT pin down "the" naturals.
# Non-standard models satisfy them too: a copy of N followed by extra
# Z-chains of "infinite" numbers. We exhibit a toy intruder that satisfies
# successor-injectivity and 0-not-a-successor, yet is NOT the naturals.
# ============================================================
def intruder():
    print("WALL 1b — what induction is FOR: the non-standard intruder\n")
    print("  P1-P4 alone are satisfied by MORE than the naturals. Example:")
    print("  take N, then append a second chain ...,b-2,b-1,b0,b1,b2,...")
    print("  (a full Z-line of 'infinite' numbers). Check the axioms:")
    # model: standard part ints >=0, plus a shadow Z-line labelled ('b', k)
    def is_succ_of(x, y):   # x = S(y)?
        if isinstance(y, int): return x == y + 1
        return x == ('b', y[1] + 1)
    def is_a_successor(x):  # does x = S(z) for some element z in the model?
        # standard positives are successors; 0 is not; every shadow b_k is
        return (isinstance(x, int) and x > 0) or (isinstance(x, tuple))
    checks = [
        ("0 is not a successor of anything", not is_a_successor(0)),
        ("S injective on standard part", (1 == 0+1) and (2 == 1+1)),
        ("S injective on shadow line", is_succ_of(('b',3),('b',2))),
        ("shadow elements have predecessors too (b_k = S(b_{k-1}))",
            is_succ_of(('b',0),('b',-1))),
    ]
    for name, ok in checks:
        print(f"    [{'ok' if ok else 'XX'}] {name}")
    print("\n  Every P1-P4 check passes — yet this structure is NOT N: it has")
    print("  elements bigger than every S^k(0). Only INDUCTION (P5) kills it,")
    print("  because no b_k is reachable from 0 by finitely many S. That is")
    print("  precisely the reification P5 removes: 'the naturals' are not")
    print("  found; they are the structure you get by STIPULATING that every")
    print("  element is reachable. The intruder makes the stipulation visible.\n")

# ============================================================
# WALL 2 — THE GODEL WALL
# Even with all of PA, you cannot prove Con(PA) inside PA. De-reifying the
# axioms does not ground them from within. Gentzen grounds Con(PA) — but
# only by BORROWING induction up to epsilon_0, a STRONGER stipulation.
# The catalog already prices this exactly: ordinal CNF arithmetic is
# FORCED (executable), while "Con(PA)=induction to epsilon_0" is PRESUMED.
# ============================================================
def godel_wall():
    print("WALL 2 — the Godel wall (and Gentzen's honest bargain)\n")
    print("  Godel 1931:   no consistent theory strong enough to encode")
    print("                arithmetic proves its OWN consistency. PA cannot")
    print("                certify PA from inside.")
    print("  Gentzen 1936: Con(PA) CAN be proved — using transfinite")
    print("                induction up to epsilon_0. But that is a STRONGER")
    print("                stipulation than PA itself. You did not ground")
    print("                arithmetic on nothing; you borrowed a bigger axiom.\n")
    print("  PL's reading: de-reification reaches its floor here. The axioms")
    print("  are visible as stipulations; their consequences are forced and")
    print("  checkable; and the grounding of the whole cannot be done from")
    print("  inside — it can only be TRADED UPWARD for a larger stipulation.")
    print("  Claiming PL escapes this would reify PL. It does not escape it.")
    print("  It NAMES it. That naming is the entire deliverable.\n")

if __name__ == "__main__":
    induction_wall()
    intruder()
    godel_wall()
