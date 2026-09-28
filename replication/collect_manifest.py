
from __future__ import annotations
import hashlib,json,os,platform,subprocess,sys
from pathlib import Path

def sha256_file(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def main():
    root=Path.cwd()
    files=[p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts]
    try: git=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception: git=os.environ.get("GITHUB_SHA","UNKNOWN")
    manifest={
        "schema_version":1,"git_commit":git,
        "environment":{"python":sys.version,"platform":platform.platform(),"machine":platform.machine()},
        "artifacts":{str(p.relative_to(root)).replace("\\","/"):sha256_file(p) for p in files if p.stat().st_size<50*1024*1024}
    }
    Path("replication_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"git_commit":git,"artifact_count":len(manifest["artifacts"])},indent=2))
if __name__=="__main__":main()
