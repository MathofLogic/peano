"""
pl_peano.py — a Process-Logic "Peano", pulled from James's diary.
==========================================================================
Classical Peano presupposes exactly what the diary forbids: discrete
objects (0, 1, 2...), intrinsic identity (S is injective — each number
is ITSELF, distinct, forever), and persistence (induction quantifies
over a fixed set of things that ARE). The diary's whole claim is that
these are reifications: "the entities are labels for stable variations
of this process across contexts."

So a PL-Peano cannot count objects. It has to build counting as what the
diary says number actually is: "labels for relational iteration
patterns," "unbounded iteration, not destination." Number is not a thing
reached; it is a PLATEAU OF ACCUMULATED LOAD in an ongoing propagation.

The dictionary of the translation:

    classical Peano            PL / diary
    ----------------           ----------------------------------------
    0                          the null propagation — zero accumulated
                               load, not an object. "before" any history.
    S (successor)              one more differential propagation: a
                               perturbation that accumulates load
    n (a number)              NOT an object. A COHERENCE PLATEAU: a
                               pattern stable at a given load-depth
    n = n (identity)           NOT intrinsic. Two propagations "are the
                               same number" iff they have equivalent
                               loaded history relative to available
                               gradients — a relation, not an essence
    S injective                NOT "distinct objects". Distinguishable
                               plateaus = different load-depth. Sameness
                               and difference are BOTH relational.
    induction                  NOT quantifying over a set of things.
                               Propagation of stability along the
                               gradient: if the null plateau is coherent
                               and coherence PROPAGATES one step, it
                               propagates along the whole gradient.
    a + b                      confluence of two loaded histories: run
                               b's accumulation onward from a's plateau
    a x b                      b-fold re-propagation of a's load

Nothing here is an object. Everything is a propagation with a load and a
coherence relation. "Numbers" are the stable variations. We then CHECK
that this process reproduces arithmetic on a finite stretch of the
gradient — and, in the diary's own spirit, we refuse to reify the
plateaus back into objects even though they behave like them.
"""
from __future__ import annotations
from dataclasses import dataclass, field


# --- a propagation is a history, not a thing ------------------------------
# We represent a propagation by its LOADED HISTORY: the sequence of
# perturbations it has accumulated. Crucially, the identity of a
# propagation is NOT the tuple itself (that would reify it) — identity is
# defined relationally below, by load-equivalence against the gradient.

@dataclass(frozen=True)
class Propagation:
    """A differential propagation carrying a loaded history.
    The history is a record of perturbation events; what MATTERS about it
    is its load-depth relative to the gradient, not its intrinsic content."""
    history: tuple = ()          # the accumulated perturbations (opaque marks)

    def perturb(self, mark="."):
        """One more differential propagation: accumulate load.
        This is the process-equivalent of 'successor' — but it is an
        ACTION on a propagation, producing a more-loaded propagation,
        never a step to a next OBJECT."""
        return Propagation(self.history + (mark,))

    def load(self, gradient=None):
        """Load = accumulated relational history relative to available
        gradients. With the trivial (uniform) gradient, load is just
        accumulated depth. With a real gradient, some marks are 'vented'
        (don't count) — see Gradient below. Load is RELATIONAL: it only
        exists relative to what the context supports."""
        if gradient is None:
            return len(self.history)
        return gradient.load_of(self.history)


# the null propagation: zero accumulated load. NOT an object called "zero"
# — the absence of history. Everything else is perturbation away from it.
NULL = Propagation(())


# --- the gradient: what the context supports ------------------------------
# The diary: "loaded history sets the gradient demands for propagation
# relative to available gradients of a context." Coherence, sameness,
# counting — all are RELATIVE to a gradient. There is no gradient-free
# fact about number. This is the anti-intrinsicality made mechanical.

@dataclass(frozen=True)
class Gradient:
    """Available gradients of a context. `vents` marks are perturbations
    the context dissipates back to simplicity (they carry no persisting
    load). The uniform gradient vents nothing — every perturbation loads.
    A structured gradient is how 'the same propagation' can have different
    load in different contexts (the diary's relativity of number)."""
    vent: frozenset = frozenset()

    def load_of(self, history):
        # load = perturbations that were NOT vented back into simplicity
        return sum(1 for m in history if m not in self.vent)


UNIFORM = Gradient()             # vents nothing: pure accumulation


# --- relational identity: sameness is a RELATION, not an essence ----------
# Two propagations "are the same number" iff they carry equivalent load
# on the gradient. Identity is coherence-of-load, never intrinsic.

def same_number(p, q, gradient=UNIFORM):
    """The de-reified '=': equivalent loaded history relative to the
    gradient. Note two DIFFERENT histories can be the same number if the
    gradient vents their difference — sameness is contextual, as the
    diary demands."""
    return p.load(gradient) == q.load(gradient)


def coheres(p, gradient=UNIFORM):
    """A propagation 'coheres' (is a stable plateau / a genuine number)
    when its load is well-defined and finite on the gradient. Every
    finite propagation coheres on UNIFORM; structured gradients can make
    some propagations fail to settle (see cascade below)."""
    return p.load(gradient) >= 0        # finite histories always settle here


# --- the operators: confluence and re-propagation -------------------------
# Not operations on objects. Confluence RUNS one loaded history onward
# from another's plateau. The diary: complexity is "gradient demands of
# loaded histories meeting the gradient demands of other loaded histories."

def confluence(a, b):
    """a (+) b : continue accumulating b's load onward from a's plateau.
    The process-equivalent of addition — but it is two propagations
    MERGING their histories, not two numbers being summed. Defined by the
    same recursion shape as Peano's +, read processually:
        a (+) null      = a           (no further perturbation: rest)
        a (+) perturb(b)= perturb(a (+) b)   (carry one more perturbation)"""
    if len(b.history) == 0:
        return a
    # peel one perturbation off b, carry it onto the confluence
    b_less = Propagation(b.history[:-1])
    return confluence(a, b_less).perturb(b.history[-1])


def repropagate(a, b):
    """a (x) b : re-run a's accumulation once per perturbation in b.
    The process-equivalent of multiplication — b-fold re-propagation of
    a's loaded history:
        a (x) null       = null
        a (x) perturb(b) = (a (x) b) (+) a"""
    if len(b.history) == 0:
        return NULL
    b_less = Propagation(b.history[:-1])
    return confluence(repropagate(a, b_less), a)


# --- induction, de-reified: PROPAGATION of coherence along the gradient ---
# Classical induction quantifies over a SET of objects that ARE. The diary
# forbids the set and the objects. So induction becomes what it always
# secretly was in process terms: if a coherence property holds at the null
# plateau, and coherence PROPAGATES across one perturbation, then — being a
# stable low-load pattern — it propagates along the entire gradient. This
# is not "true of all n". It is "this coherence is a fast, low-load pattern
# that the gradient carries outward without drag".

def coherence_propagates(prop_of_plateau, depth, gradient=UNIFORM):
    """prop_of_plateau: a predicate on a propagation (a coherence claim).
    Returns whether the coherence holds at NULL and survives each
    perturbation up to `depth`. This is the ENGINE of induction read as
    propagation: we watch the coherence ride the gradient outward. It is
    evidence of propagation, not a proof over a completed infinity — the
    diary has no completed infinities, only 'unbounded iteration'."""
    p = NULL
    if not prop_of_plateau(p):
        return False, "coherence fails at the null plateau"
    for k in range(depth):
        nxt = p.perturb()
        if not (prop_of_plateau(nxt) if prop_of_plateau(p) else True):
            return False, f"coherence fails to propagate at load {k+1}"
        p = nxt
    return True, f"coherence propagated to load {depth} without drag"


# --- cascade collapse: the diary's own dynamics, kept faithful ------------
# The diary insists complexity builds relational drag and, past a boundary,
# "reconfigures to simpler more relationally coherent structuring." A number
# system that ONLY accumulates would be a reification of unbounded object-
# hood. So we honour the process: on a gradient with a stability boundary,
# a propagation whose load exceeds the boundary VENTS simplicity — it does
# not grow without limit as an object would; it reconfigures.

@dataclass(frozen=True)
class BoundedGradient:
    """A context with finite stability room. Load beyond `boundary`
    triggers reconfiguration: the propagation sheds simplicity back into
    the field (cascade), landing on a lower-load coherent plateau. This is
    modular-arithmetic-like, but it is NOT 'numbers mod n' as objects — it
    is a propagation venting under drag, per the diary's cascade."""
    boundary: int

    def settle(self, p: Propagation):
        load = len(p.history)
        if load <= self.boundary:
            return p, "stable: within coherence gradient"
        # cascade: vent simplicity until back under the boundary
        vented = load % (self.boundary + 1)
        return Propagation(('.',) * vented), \
            f"cascade: load {load} exceeded boundary {self.boundary}, " \
            f"reconfigured to load {vented}"
