
# RVP-1 evaluator brief

## What an external evaluator can run immediately

1. Execute the RVP-1 conformance workflow.
2. Inspect the formal reference state machine and TLA+ model.
3. Run the raw-frame whitelist/reassembly tests.
4. Run the hostile-prover benchmark with fixed seeds.
5. Run the interval-valued compute-accounting tests.
6. Run the integrated retrofit readiness report.
7. Inspect provenance gates showing exactly which claims cannot yet be promoted.

## Research questions the package is designed to answer

- How much capture bandwidth is required at each line rate?
- What happens when a packet is omitted, substituted, rebound, or selected around?
- What detection probability follows from a declared sampling rate and attack size?
- Which timing/header/payload channels remain under a proposed gateway policy?
- What residual compute can be bounded from interval-valued supply-chain evidence?
- What measurements must a real tap, capture server, memory-wipe system or warden
  produce before a software result can become a physical claim?
- Can an independent lab reproduce the result from the same commit, seed and
  raw artifacts?

## Explicit non-claims

The package does not claim to have physically validated 1600G capture, defeated
nation-state tampering, proven complete global chip accounting, or solved
frontier-scale cryptographic workload proofs.

Those are treated as external acceptance gates rather than filled with synthetic
numbers.

## Why this is useful to the field

AI Futures describes the central near-term verification proposal as passive
network taps feeding trusted servers for random partial recomputation and lists
open problems in physical-layer monitoring, covert channels, cryptographic proof
and trust-root composition. RVP-1 exposes each of these as an interface with a
clear evidence-promotion rule, making it straightforward for another lab to
replace a simulator component with a real measurement and rerun the same claims.
