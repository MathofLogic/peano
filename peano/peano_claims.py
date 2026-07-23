"""
peano_claims.py — the ledger for the de-reified Peano carrier.
==========================================================================
Priced in PL currency. FORCED-on-cut = enumerated on a finite cut V_N
(genuine evidence for an equational law, explicitly NOT the universal
theorem). STIPULATED = a chosen axiom/schema, offered not discovered.
PRESUMED/CITED = a meta-theorem no instance can exhibit. The paid
fraction is honest: the ring laws are checkable; the grounding is not.
"""

SECTIONS = [
    ("The axioms, as stipulations (theta)", [
        {"claim": "0 is a chosen origin (P1); V is closed under S (P2) — "
                  "the value space is GENERATED from these, not presupposed",
         "tier": "STIPULATED", "cite": "peano_carrier.AXIOMS"},
        {"claim": "S is injective and 0 is no successor (P3,P4) — the tower "
                  "has a floor and never merges",
         "tier": "STIPULATED", "cite": "peano_carrier.AXIOMS"},
        {"claim": "induction (P5) is a SCHEMA — one axiom per predicate, an "
                  "infinite family — and it is the theta that fixes which "
                  "structure counts",
         "tier": "STIPULATED", "cite": "peano_carrier.AXIOMS / walls.induction_wall"},
    ]),
    ("The arithmetic, DERIVED and enumerated (forced on the cut)", [
        {"claim": "+ and x are defined by recursion on S, not assumed",
         "tier": "STIPULATED", "cite": "peano_carrier.add/mul (the defining equations)"},
        {"claim": "+ and x form a commutative semiring: commutativity, "
                  "associativity, distributivity all hold on V_6",
         "check": "derive.run", "tier": "FORCED-on-cut"},
        {"claim": "S injective and the recursion equations hold on V_6",
         "check": "derive.run", "tier": "FORCED-on-cut"},
    ]),
    ("The walls, named not hidden", [
        {"claim": "a finite cut is EVIDENCE not PROOF: lifting FORCED-on-cut "
                  "to FORCED needs induction, which no enumeration closes",
         "tier": "STIPULATED", "cite": "walls.induction_wall"},
        {"claim": "P1-P4 alone admit non-standard intruders; only P5 excludes "
                  "them — 'the naturals' are stipulated-reachable, not found",
         "check": "walls.intruder", "tier": "FORCED-on-cut"},
        {"claim": "Con(PA) is not provable in PA (Godel 1931)",
         "tier": "PRESUMED", "cite": "Godel 1931 — meta-theorem, not enumerable"},
        {"claim": "Con(PA) = transfinite induction to epsilon_0 (Gentzen); the "
                  "ordinal CNF arithmetic underneath is executable, the "
                  "equivalence itself is not",
         "tier": "PRESUMED", "cite": "Gentzen 1936; ORDINALS carrier is FORCED, the reduction is PRESUMED"},
    ]),
    ("The anti-reification of PL itself", [
        {"claim": "de-reifying PA does NOT ground it; PL names the seam "
                  "(Wall 2) rather than claiming to cross it — claiming "
                  "otherwise would reify PL",
         "tier": "STIPULATED", "cite": "walls.godel_wall"},
    ]),
]
