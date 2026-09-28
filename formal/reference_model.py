
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class Phase(Enum): OPEN="OPEN"; COMMITTED="COMMITTED"; CHALLENGED="CHALLENGED"; CHECKED="CHECKED"; TERMINAL="TERMINAL"

@dataclass
class State:
    phase:Phase=Phase.OPEN
    claim_root:str|None=None
    challenge:str|None=None
    result:str|None=None

def commit(s:State,claim_root:str):
    if s.phase is not Phase.OPEN: raise ValueError("commit only from OPEN")
    s.claim_root=claim_root;s.phase=Phase.COMMITTED
def challenge(s:State,challenge_id:str):
    if s.phase is not Phase.COMMITTED: raise ValueError("challenge only after commitment")
    s.challenge=challenge_id;s.phase=Phase.CHALLENGED
def check(s:State,result:str):
    if s.phase is not Phase.CHALLENGED: raise ValueError("check only after challenge")
    if result not in {"PASS","FAIL","UNKNOWN"}: raise ValueError("bad result")
    s.result=result;s.phase=Phase.CHECKED
def terminalize(s:State):
    if s.phase is not Phase.CHECKED: raise ValueError("terminalize only after check")
    s.phase=Phase.TERMINAL

def safety_invariants(s:State)->list[str]:
    errors=[]
    if s.phase in {Phase.CHALLENGED,Phase.CHECKED,Phase.TERMINAL} and not s.claim_root: errors.append("no commitment")
    if s.phase in {Phase.CHECKED,Phase.TERMINAL} and not s.challenge: errors.append("no challenge")
    if s.phase is Phase.TERMINAL and s.result=="PASS" and not s.claim_root: errors.append("PASS without commitment")
    return errors
