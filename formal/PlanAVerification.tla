---- MODULE PlanAVerification ----
EXTENDS Naturals, TLC

CONSTANTS Sites, Packets, Verifiers

VARIABLES phase, commitment, challenge, result, evidence

Phases == {"OPEN", "COMMITTED", "CHALLENGED", "CHECKED", "TERMINAL"}
Results == {"PASS", "FAIL", "UNKNOWN", "NONE"}

Init ==
    /\ phase = "OPEN"
    /\ commitment = ""
    /\ challenge = ""
    /\ result = "NONE"
    /\ evidence = {}

Commit(c) ==
    /\ phase = "OPEN"
    /\ c # ""
    /\ commitment' = c
    /\ phase' = "COMMITTED"
    /\ UNCHANGED <<challenge, result, evidence>>

Reveal(ch) ==
    /\ phase = "COMMITTED"
    /\ ch # ""
    /\ challenge' = ch
    /\ phase' = "CHALLENGED"
    /\ UNCHANGED <<commitment, result, evidence>>

Check(r, e) ==
    /\ phase = "CHALLENGED"
    /\ r \in Results \ {"NONE"}
    /\ result' = r
    /\ evidence' = e
    /\ phase' = "CHECKED"
    /\ UNCHANGED <<commitment, challenge>>

Finalize ==
    /\ phase = "CHECKED"
    /\ phase' = "TERMINAL"
    /\ UNCHANGED <<commitment, challenge, result, evidence>>

Next ==
    \/ \E c \in STRING : Commit(c)
    \/ \E ch \in STRING : Reveal(ch)
    \/ \E r \in Results, e \in SUBSET Packets : Check(r, e)
    \/ Finalize

Spec == Init /\ [][Next]_<<phase, commitment, challenge, result, evidence>>

CommitBeforeChallenge ==
    phase \in {"CHALLENGED", "CHECKED", "TERMINAL"} => commitment # ""

NoPassWithoutEvidence ==
    result = "PASS" => Cardinality(evidence) > 0

ChallengeBeforeCheck ==
    phase \in {"CHECKED", "TERMINAL"} => challenge # ""

Safety == CommitBeforeChallenge /\ NoPassWithoutEvidence /\ ChallengeBeforeCheck

====
