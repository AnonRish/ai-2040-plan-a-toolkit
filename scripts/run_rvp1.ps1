$ErrorActionPreference = "Stop"

python -m pip install -r requirements.txt
python -m pytest plan_a_protocol/tests embedded_audit/tests verification_lab/tests frame_processor/tests hostile_prover/tests formal/test_reference_model.py benchmarks/test_benchmark.py benchmarks/test_scorecard.py benchmarks/test_compare.py compute_accounting/test_interval_ledger.py gateway/test_policy.py gateway/test_active_contract.py provenance/test_gate.py assurance/test_compose.py assurance/test_sampling_economics.py crypto/test_proof_envelope.py hardware/test_live_capture_import.py deployment/test_readiness.py telemetry/test_consistency.py storage/test_weight_path.py redteam/test_scenarios.py redteam/test_integrated.py track3/test_tail_audit.py -q
python -m benchmarks.benchmark
python -m hostile_prover.run_benchmark
python -m verification_lab.run_report
python -m replication.collect_manifest

Write-Host ""
Write-Host "RVP-1 research package completed. Review:"
Write-Host "  benchmark_result.json"
Write-Host "  adversarial_results.json"
Write-Host "  retrofit_readiness_report.json"
Write-Host "  replication_manifest.json"
