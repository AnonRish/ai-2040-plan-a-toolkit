
from .reference_model import *
def test_phase_order_and_invariants():
    s=State();commit(s,"root");challenge(s,"c");check(s,"PASS");assert not safety_invariants(s);terminalize(s);assert s.phase is Phase.TERMINAL
def test_invalid_transition_is_rejected():
    s=State()
    try: check(s,"PASS")
    except ValueError: pass
    else: assert False
