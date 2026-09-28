
from verification_lab.retrofit import RetrofitConfig, run_retrofit_simulation
from verification_lab.core import rogue_work_for_confidence

def test_plan_a_2034_assurance_target():
    required_packets = 46000 / 100
    assert rogue_work_for_confidence(0.99, 0.01) <= required_packets + 1

def test_integrated_retrofit_simulation_is_not_allowed_to_claim_complete():
    result = run_retrofit_simulation(RetrofitConfig(capture_servers=10))
    assert result["workstream_1_tap"]["status"] == "PASS"
    assert result["workstream_7_sampling"]["detection_confidence_at_target"] > 0.99
    assert result["workstream_17_completeness"]["status"] == "UNKNOWN"
    assert result["global_status"] == "PARTIAL"
