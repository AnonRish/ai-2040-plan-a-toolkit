from __future__ import annotations
from pathlib import Path
import json

REQUIRED_FILES=('RVP-1.md','BENCHMARK_PROTOCOL.md','EVALUATOR_BRIEF.md','verification_lab/workstreams.json','.github/workflows/rvp-conformance.yml','scripts/run_rvp1.ps1')
REQUIRED_PACKAGES=('plan_a_protocol','embedded_audit','verification_lab','frame_processor','hostile_prover','formal','benchmarks','compute_accounting','gateway','provenance','assurance','crypto','hardware','deployment','telemetry','storage','redteam','track3','adversary','capture_benchmark')

def validate_repository(root:str='.'):
    base=Path(root); errors=[]
    for path in REQUIRED_FILES:
        if not (base/path).exists(): errors.append(f'missing required file: {path}')
    for package in REQUIRED_PACKAGES:
        if not (base/package/'__init__.py').exists(): errors.append(f'missing package init: {package}')
    json_files=list(base.glob('**/*.json')); bad=[]
    for path in json_files:
        try: json.loads(path.read_text(encoding='utf-8'))
        except Exception: bad.append(str(path))
    if bad: errors.append('invalid JSON: '+', '.join(bad))
    return {'status':'PASS' if not errors else 'FAIL','required_file_count':len(REQUIRED_FILES),'package_count':len(REQUIRED_PACKAGES),'json_files_checked':len(json_files),'errors':errors}

if __name__=='__main__': print(json.dumps(validate_repository(),indent=2))
