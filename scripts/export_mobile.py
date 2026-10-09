"""Export only explicit research context; no network or third-party packages."""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ["research/BRIEF.md", "research/STATE.md", "research/protocol.md",
             "research/sources.csv", "research/claims.csv"]

def export(root, revision):
    if not revision or "\n" in revision or "\r" in revision:
        raise ValueError("Supply a single-line base revision")
    mobile = root / "mobile"
    mobile.mkdir(exist_ok=True)
    manifest = {"base_revision": revision, "files": {}}
    chunks = ["# Context snapshot", "Base revision: " + revision,
              "Uploads are snapshots. Do not assume access to other repository files."]
    for rel in ALLOWLIST:
        path = root / rel
        if path.is_symlink() or root.resolve() not in path.resolve().parents:
            raise ValueError("Context file must remain within project")
        raw = path.read_bytes()
        manifest["files"][rel] = hashlib.sha256(raw).hexdigest()
        chunks += ["\n## " + rel, raw.decode("utf-8")]
    (mobile / "CONTEXT.md").write_text("\n".join(chunks), encoding="utf-8")
    (mobile / "snapshot.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    parts = ["# Mobile Research Kit", "Policies and workflows, not executable mobile plugins."]
    paths = [root / "AGENTS.md", root / "docs/EVIDENCE.md"]
    paths += sorted((root / ".agents/skills").glob("*/SKILL.md"))
    paths += sorted((root / "templates").glob("*"))
    for path in paths:
        if path.is_symlink() or root.resolve() not in path.resolve().parents:
            raise ValueError("Kit file must remain within project")
        parts += ["\n## " + path.relative_to(root).as_posix(), path.read_text(encoding="utf-8")]
    (mobile / "MOBILE-KIT.md").write_text("\n".join(parts), encoding="utf-8")
    return manifest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()
    export(ROOT, args.revision)
    print("Exported allowlisted context and kit. Review before uploading.")

