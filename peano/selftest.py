"""selftest.py — the de-reified Peano build gates itself."""
import sys
from derive import run, LAWS, check
from walls import induction_wall, intruder, godel_wall
from peano_carrier import add, mul, nat, Z, S

def expect(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    return cond

def main():
    ok = True
    print("De-reified Peano — self-test\n")
    # 1. the carrier computes
    ok &= expect("2+3=5 and 2*3=6 by recursion on S",
                 int(add(nat(2),nat(3)))==5 and int(mul(nat(2),nat(3)))==6)
    # 2. numbers ARE constructions (de-reification visible)
    ok &= expect("3 is literally S^3(0), not an atom", repr(nat(3))=="S^3(0)")
    # 3. all ring laws forced on the cut
    allok = all(check(n,l,6)[0] for n,l in LAWS.items())
    ok &= expect("commutative semiring laws FORCED on V_6", allok)
    # 4. VACUITY GUARD: a FALSE law must actually fail on the cut
    bad = lambda a,b,c: int(add(a,b))==int(a)  # a+b=a  (false for b>0)
    bad_fails, _ = check("bogus", bad, 4)
    ok &= expect("a false law is caught by the cut (non-vacuous)", not bad_fails)
    # 5. the walls run and stay honest
    try:
        induction_wall(); intruder(); godel_wall()
        ok &= expect("both walls exhibited without crashing", True)
    except Exception as e:
        ok &= expect(f"walls run ({e})", False)
    print()
    print("SELF-TEST GREEN — arithmetic derived, walls named."
          if ok else "SELF-TEST RED")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
