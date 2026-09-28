
import math
from assurance.sampling_economics import SamplingPlan, compare_to_budget

def test_plan_a_style_example():
    p=SamplingPlan(.01,100,0.99,46000)
    r=compare_to_budget(p)
    assert math.isclose(r["required_verified_packets"],460.51701859880916,rel_tol=1e-10)
    assert r["meets_target"] is False
    assert r["achieved_confidence"]>0.989

def test_budget_equation_is_positive():
    p=SamplingPlan(.02,50,.95,0)
    assert p.required_rogue_compute()>0
