
# RVP-1 evaluator brief

## What an external evaluator can run immediately

1. Execute the RVP-1 conformance workflow.
2. Inspect the formal reference state machine and TLA+ model.
3. Run raw Ethernet frame parsing, whitelist enforcement and TCP reassembly tests.
4. Run the hostile-prover benchmark with fixed seeds.
5. Run interval-valued compute-accounting and telemetry consistency tests.
6. Run the integrated retrofit readiness report.
7. Inspect evidence provenance gates and the field deployment playbook.

## Research questions

The package is designed to answer concrete questions across all four tracks:
capture and reconstruction; reproducibility; random recomputation; adversarial
cheating; physical installation integrity; reporting integrity; memory wipe and
side-channel controls; secret-compute accounting; workload classification; trust
composition; cryptographic proof interfaces; manufacturing and deployment
readiness; and independent replication.

## Measurement discipline

External hardware results must report raw data, environment, parameters, seeds,
device IDs and hashes. Synthetic results remain synthetic. A benchmark is not
promoted simply because it looks plausible or agrees with the author's model.

## Explicit non-claims

The package does not claim to have physically validated 1600G capture, defeated
nation-state tampering, proven complete global chip accounting, or solved
frontier-scale cryptographic workload proofs.

Those are external acceptance gates.
