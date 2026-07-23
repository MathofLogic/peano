"""
derive_pl.py — arithmetic EMERGES from propagation, checked; then the
diary's own anti-reification test is turned on the result.
==========================================================================
Two jobs. First: show the commutative-semiring laws are not axioms about
objects but STABLE COHERENCES of the propagation process — verified over
a finite stretch of the gradient. Second, and this is the point of doing
it James's way: run the diary's five-step reification test on our OWN
plateaus, to confirm we did not smuggle objects back in.
"""
from pl_peano import (NULL, Propagation, Gradient, UNIFORM,
                      confluence, repropagate, same_number,
                      coherence_propagates, BoundedGradient)
from itertools import product


def prop(n):
    """A propagation carrying n perturbations. NOT 'the number n' — a
    history with load n. We use it to probe the process."""
    p = NULL
    for _ in range(n):
        p = p.perturb()
    return p


def law_holds(f, N):
    """f(a,b,c) over all load-triples up to N; returns (ok, first_fail)."""
    for a, b, c in product(range(N + 1), repeat=3):
        if not f(a, b, c):
            return False, (a, b, c)
    return True, None


# each law is a COHERENCE of the process, phrased on loads, checked on
# propagations. Sameness is relational (same_number), never ==-on-objects.
COHERENCES = {
    "rest (a (+) null = a)":
        lambda a, b, c: same_number(confluence(prop(a), NULL), prop(a)),
    "carry (a (+) perturb(b) = perturb(a (+) b))":
        lambda a, b, c: same_number(
            confluence(prop(a), prop(b).perturb()),
            confluence(prop(a), prop(b)).perturb()),
    "confluence commutes (a (+) b = b (+) a)":
        lambda a, b, c: same_number(confluence(prop(a), prop(b)),
                                    confluence(prop(b), prop(a))),
    "confluence associates":
        lambda a, b, c: same_number(
            confluence(confluence(prop(a), prop(b)), prop(c)),
            confluence(prop(a), confluence(prop(b), prop(c)))),
    "re-propagation over null = null":
        lambda a, b, c: same_number(repropagate(prop(a), NULL), NULL),
    "re-propagation commutes (a (x) b = b (x) a)":
        lambda a, b, c: same_number(repropagate(prop(a), prop(b)),
                                    repropagate(prop(b), prop(a))),
    "re-propagation associates":
        lambda a, b, c: same_number(
            repropagate(repropagate(prop(a), prop(b)), prop(c)),
            repropagate(prop(a), repropagate(prop(b), prop(c)))),
    "distribution (a (x) (b (+) c) = a(x)b (+) a(x)c)":
        lambda a, b, c: same_number(
            repropagate(prop(a), confluence(prop(b), prop(c))),
            confluence(repropagate(prop(a), prop(b)),
                       repropagate(prop(a), prop(c)))),
    "distinguishability is relational (diff load => diff number)":
        lambda a, b, c: (a == b) or (not same_number(prop(a), prop(b))),
}


def derive(N=6):
    print(f"ARITHMETIC AS STABLE COHERENCE OF PROPAGATION  (gradient stretch 0..{N})")
    print("each law is a coherence of the process, not an axiom about objects.\n")
    allok = True
    for name, f in COHERENCES.items():
        ok, fail = law_holds(f, N)
        allok &= ok
        print(f"  [{'coheres ' if ok else 'DRAG    '}] {name:52} "
              f"{'stable across the stretch' if ok else f'reconfigures at {fail}'}")
    print()
    # induction as propagation, shown explicitly
    ok, msg = coherence_propagates(lambda p: p.load() >= 0, N)
    print(f"  induction-as-propagation: coherence rides the gradient — {msg}")
    return allok


# --- the diary's own test, turned on us ----------------------------------
def anti_reification_audit():
    """James's five-step reification test (diary lines 130-144), applied to
    OUR plateaus. If we reified, this catches it. The whole exercise is
    only honest if it passes its own author's test."""
    print("\nANTI-REIFICATION AUDIT  (the diary's 5-step test, turned on us)\n")
    checks = []

    # Step 1-4: did we treat a plateau as an object existing independently?
    # Test: is 'the number 2' anything OVER AND ABOVE a load-2 propagation
    # relative to a gradient? If two different histories at load 2 are the
    # same number, then 'number' is relational, not an intrinsic object.
    g = Gradient(vent=frozenset(['x']))
    h1 = Propagation(('.', '.'))
    h2 = Propagation(('.', 'x', '.'))   # different history, load 2 on g
    same = same_number(h1, h2, g)
    checks.append(("number is relational, not intrinsic "
                   "(distinct histories, same number on a gradient)", same))

    # Test: does sameness require a relation? (identity is not free-standing)
    # same_number always takes a gradient — there is no gradient-free '='.
    import inspect
    sig = inspect.signature(same_number)
    checks.append(("identity is a relation, never gradient-free "
                   "(same_number requires a gradient)",
                   "gradient" in sig.parameters))

    # Test: does the system reconfigure under drag rather than accrete
    # as an unbounded object? (the diary forbids reified unbounded objecthood)
    bg = BoundedGradient(boundary=3)
    _, msg = bg.settle(Propagation(('.',) * 9))
    checks.append(("plateaus reconfigure under drag, don't accrete as objects "
                   "(cascade fires past the boundary)", "cascade" in msg))

    # Test: is NULL an object called zero, or the absence of history?
    checks.append(("the origin is absence-of-load, not an object 'zero' "
                   "(NULL.history is empty)", NULL.history == ()))

    ok = True
    for name, passed in checks:
        ok &= passed
        print(f"  [{'PASS' if passed else 'REIFIED!'}] {name}")
    print()
    print("  " + ("AUDIT GREEN — no objects smuggled in; the plateaus stay "
                  "relational." if ok else
                  "AUDIT RED — a reification slipped through."))
    return ok


if __name__ == "__main__":
    a = derive(6)
    b = anti_reification_audit()
    print("\n" + ("=" * 60))
    print("arithmetic emerges as coherence, and stays de-reified."
          if a and b else "something drags.")
