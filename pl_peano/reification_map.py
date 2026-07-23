"""
reification_map.py — each classical Peano axiom shown as a REIFIED
process coherence. The diary's central claim, made concrete and testable.
==========================================================================
The diary (lines 130-144): reification = "take something that only exists
through relations and treat it as if it exists independently. Make a verb
into a noun. Turn a pattern into a substance." Classical Peano is,
on this reading, exactly that move applied to counting. Here is the map,
verb-side and noun-side, with the process fact that the noun-side reifies.
"""
from pl_peano import (NULL, Propagation, confluence, repropagate,
                      same_number, coherence_propagates)

MAP = [
    ("P1: 0 is an object (a number).",
     "the NULL propagation: absence of accumulated load.",
     "0 is not a thing; it is where load has not yet accumulated. "
     "Reifying the absence into an object 'zero' is step 1 of the diary's "
     "test — a pattern turned into a substance."),
    ("P2: every number has a successor S(n).",
     "propagation can always accept one more perturbation.",
     "'successor' reifies the ACT of perturbing into a step-to-a-next-"
     "OBJECT. Verb (perturb) frozen into noun-sequence (the numbers)."),
    ("P3: 0 is not the successor of any number.",
     "the null plateau has no prior perturbation to have come from.",
     "a relational fact (nothing vented into it) read as an intrinsic "
     "property of an object 'zero'."),
    ("P4: S is injective (distinct numbers, distinct successors).",
     "distinguishability of plateaus is difference of load on a gradient.",
     "reifies relational distinguishability into INTRINSIC identity — the "
     "diary's 'discrete identity over time', the core classicality it says "
     "every paradox secretly assumes."),
    ("P5: induction over all numbers.",
     "coherence propagates along the gradient without drag.",
     "reifies 'a low-load pattern the gradient carries outward' into "
     "'a completed totality of all objects quantified at once'. Unbounded "
     "iteration (verb) frozen into infinite set (noun)."),
]


def show():
    print("CLASSICAL PEANO AS REIFIED PROCESS  (the diary's claim, mapped)\n")
    for i, (noun, verb, gloss) in enumerate(MAP, 1):
        print(f"  {noun}")
        print(f"    process (verb-side): {verb}")
        print(f"    the reification:     {gloss}\n")


def demonstrate_the_reification_is_optional():
    """The strong claim: you can DO all of arithmetic on the verb-side,
    never reifying. We already did (derive_pl). This function makes the
    point pointed: the SAME computation, 2+3=5, done purely as confluence
    of histories, with sameness relational — no object ever named."""
    print("PROOF THE NOUN-SIDE IS OPTIONAL: 2 (+) 3 with no objects\n")
    a = NULL.perturb().perturb()          # a history at load 2
    b = NULL.perturb().perturb().perturb()  # a history at load 3
    r = confluence(a, b)
    print(f"    confluence of a load-2 history and a load-3 history")
    print(f"    settles at load {r.load()} — and we verify it is 'five'")
    print(f"    only RELATIONALLY: same_number(result, load-5 history) = "
          f"{same_number(r, Propagation(('.',)*5))}")
    print(f"    at no point did an object '2', '3', or '5' exist.")
    print(f"    there were propagations, loads, and a coherence relation.\n")


# --- the honest seam (GL-style) ------------------------------------------
def the_seam():
    """Where this stops, named. Two honesties the diary's own rigor demands."""
    print("THE SEAM  (named, not crossed)\n")
    print("  1. We check coherences on a FINITE STRETCH of the gradient.")
    print("     'Coherence propagates without drag' is shown to load N; the")
    print("     unbounded claim is the diary's 'unbounded iteration', which")
    print("     is a PROCESS never a completed set. We do not (cannot) verify")
    print("     a finished infinity — and the diary would call doing so a")
    print("     reification. The finite check is honest; the leap is process,")
    print("     not proof.\n")
    print("  2. This does NOT prove process-metaphysics is 'how reality is'.")
    print("     It shows arithmetic CAN be built with no objects, discreteness,")
    print("     or intrinsicality — that the reification is OPTIONAL, not that")
    print("     it is false. Claiming the diary's frame is THE truth would")
    print("     reify the diary, the one move it spends its last line refusing:")
    print("     'Parsimony achieved perhaps but not reified.' We hold to that.")


if __name__ == "__main__":
    show()
    demonstrate_the_reification_is_optional()
    the_seam()
