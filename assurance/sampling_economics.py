
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass(frozen=True)
class SamplingPlan:
    fake_fraction: float
    packet_h100e_hours: float
    confidence: float
    verifier_budget_h100e_hours: float

    def required_verified_packets(self)->float:
        if not 0<self.fake_fraction<=1 or not 0<self.confidence<1:
            raise ValueError("invalid fraction/confidence")
        return -math.log(1-self.confidence)/self.fake_fraction

    def required_rogue_compute(self)->float:
        return self.required_verified_packets()*self.packet_h100e_hours

    def achieved_confidence(self)->float:
        if self.packet_h100e_hours<=0 or self.verifier_budget_h100e_hours<0:
            raise ValueError("invalid packet/budget")
        verified=self.verifier_budget_h100e_hours/self.packet_h100e_hours
        return 1-math.exp(-self.fake_fraction*verified)

def compare_to_budget(plan:SamplingPlan)->dict:
    required=plan.required_rogue_compute()
    return {
        "required_verified_packets":plan.required_verified_packets(),
        "required_verifier_budget_h100e_hours":required,
        "available_verifier_budget_h100e_hours":plan.verifier_budget_h100e_hours,
        "achieved_confidence":plan.achieved_confidence(),
        "meets_target":plan.verifier_budget_h100e_hours>=required,
    }
