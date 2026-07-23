# De-reifying Peano, and deriving arithmetic with PL

## What "de-reify" means here — and what it can't mean

Peano Arithmetic is usually met as a *discovery*: here are the natural
numbers, here are the true facts about them, go prove theorems. Process
Logic reads it as a *choice*. Not a wrong choice — an extraordinarily
good one — but a choice, with the same three moving parts every carrier
has:

- **V** (the value space): whatever the successor operator `S` generates
  starting from `0`.
- **G** (the operators): `S` first, then `+` and `×` *defined* by
  recursion on `S` — installed by equations, not found lying around.
- **θ** (the threshold): the induction schema, the stipulation that
  fixes *which* structure counts and rules out the impostors.

The de-reification is the move from "the numbers exist and we study them"
to "these axioms are stipulations, and arithmetic is what they *force*."
In the code, this is literally visible: the number 3 is not an atom. It
is `S^3(0)` — a construction with a history. Print it and you see the
tower.

There is a version of this exercise that would be a lie, and it is worth
naming so you can see this one refuses it. The lie is: *"PL dissolves the
reification — arithmetic is really just process, and Peano's mistake is
corrected."* That would reify PL. It also collides with the hardest fact
in the area (Gödel), which no reframing escapes. So this build does the
honest thing instead: it makes the stipulations **visible**, derives and
**checks** their consequences, and **names the exact seam** where
grounding stops — rather than pretending to cross it.

## The derivation: arithmetic as receipts, not axioms

The whole commutative semiring of arithmetic falls out of `0`, `S`, and
two recursion equations each for `+` and `×`. None of the ring laws are
assumed. Each is a *consequence* — a receipt you read off after the
operators are wired.

```
a + 0   = a                a × 0   = 0
a + S(b) = S(a + b)        a × S(b) = (a × b) + a
```

Run `derive.py` and every law — commutativity, associativity,
distributivity, successor-injectivity — verifies by enumeration on a
finite cut `V_6 = {0..6}`. The output labels each one **FORCED-on-cut**,
and that hyphenated tier is doing deliberate work: it means "the machine
checked every tuple in the cut and the law held," which is genuine
evidence, and it is *not the same* as the universal theorem. Conflating
those two is exactly the overclaim this vocabulary exists to prevent.

## Wall 1 — the induction wall

`a + b = b + a` held for every pair in `{0..6}`. Is it *proven*? No. A
finite cut cannot certify a statement about an unbounded `V`. To lift
**FORCED-on-cut** to **FORCED**, you need P5, induction — and induction
is a *schema*: one axiom per predicate, an infinite family. No
enumeration closes an infinite family of axioms. The theta is precisely
the stipulation that leaps from "holds for every case I checked" to
"holds for all n," and `walls.py` shows that leap for what it is: a
chosen rule discharging the gap, not a fact found at the bottom of it.

## Wall 1b — the intruder that makes the stipulation visible

Here is the sharpest single demonstration that "the naturals" are
stipulated rather than found. Take axioms P1–P4 *without* induction. They
are satisfied by more than the naturals: append to `N` a whole extra
`Z`-line of "infinite" numbers `…, b₋₁, b₀, b₁, …`, each the successor of
the last. Check the axioms against this structure:

```
[ok] 0 is not a successor of anything
[ok] S injective on the standard part
[ok] S injective on the shadow line
[ok] shadow elements have predecessors too
```

Every P1–P4 check *passes* — yet this is not `N`. It contains elements
larger than every `S^k(0)`. Only **induction** excludes it, because no
`b_k` is reachable from `0` by finitely many applications of `S`. That is
the reification P5 removes, made concrete: the naturals are not a found
object that the axioms describe. They are the structure you *get* by
stipulating that every element is reachable from `0`. The intruder is
what "reachability" is quietly buying you, dragged into the open.

## Wall 2 — the Gödel wall, and Gentzen's honest bargain

Even with all of PA, you cannot prove `Con(PA)` inside PA — Gödel, 1931.
De-reifying the axioms does not ground them from within. You can see the
temptation here to declare that PL, standing outside, supplies the
grounding PA lacked. It does not, and claiming it did would be the whole
error in one move.

What actually happens is Gentzen's bargain (1936): `Con(PA)` *can* be
proved — using transfinite induction up to the ordinal ε₀. But that is a
*stronger* stipulation than PA itself. You did not ground arithmetic on
nothing; you traded PA's stipulation for a larger one. The carrier
catalog already prices this with the exact honesty required: the ordinal
arithmetic underneath (Cantor normal form, `1+ω=ω` yet `ω+1>ω`) is
**FORCED** — executable, checkable — while the reduction "Con(PA) =
induction to ε₀" is **PRESUMED**, a proof-theoretic meta-result no
instance can exhibit.

So PL's reading reaches its floor here, and says so:

> The axioms are visible *as* stipulations. Their consequences are forced
> and checkable. The grounding of the whole cannot be done from inside —
> it can only be traded upward for a larger stipulation. Claiming PL
> escapes this would reify PL. It does not escape it. It *names* it. That
> naming is the entire deliverable.

## The ledger, and why 27% is the honest number

The claims ledger (`peano_claims.py`) prices eleven load-bearing claims.
Only three are check-backed — a paid fraction of **27%** — and that low
number is the correct one, not a weakness. Most of the ledger is
*stipulations* (the axioms, offered not discovered) and *meta-theorems*
(Gödel, Gentzen — true, cited, and by their nature not enumerable). A
ledger that marked these "verified" would be lying about the two things
that matter most. The arithmetic that *can* be enumerated is; the
grounding that cannot be is marked PRESUMED and pointed at its source.
The split *is* the de-reification: it shows you exactly where forced
consequence ends and chosen stipulation begins.

## What you actually have

- `peano_carrier.py` — `V`, `G`, `θ` for PA; numbers as explicit `S`
  towers; `+`, `×` by recursion. The de-reification is visible in the
  types.
- `derive.py` — the commutative-semiring laws derived and enumerated on
  the cut, each labelled FORCED-on-cut.
- `walls.py` — the induction wall, the non-standard intruder, and the
  Gödel/Gentzen wall, all exhibited.
- `peano_claims.py` — the honest ledger (27% paid, and that's the point).
- `selftest.py` — gates the whole thing, including a vacuity guard that
  confirms a *false* law actually fails on the cut (so the checks aren't
  rubber stamps).

Run `python selftest.py` to see it all green. The one sentence to carry
out: **de-reifying Peano does not ground arithmetic — it makes the
stipulations visible, forces and checks their consequences, and names the
seam where grounding can only be traded upward. Doing less would miss the
point; doing more would reify PL.**
