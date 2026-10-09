"""Offline structural evidence audit. Does not verify scientific truth."""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def audit(root):
    errors = []
    sources = rows(root / "research/sources.csv")
    claims = rows(root / "research/claims.csv")
    ids = {}
    for row in sources:
        eid = row.get("evidence_id", "")
        if not re.fullmatch(r"E[0-9]+", eid) or eid in ids:
            errors.append("Invalid or duplicate evidence ID: " + eid)
        ids[eid] = row
        if row.get("source_status") not in {"UNVERIFIED", "METADATA_MATCHED", "CONTENT_OPENED"}:
            errors.append(eid + ": invalid source status")
    seen = set()
    for row in claims:
        cid = row.get("claim_id", "")
        if not re.fullmatch(r"C[0-9]+", cid) or cid in seen:
            errors.append("Invalid or duplicate claim ID: " + cid)
        seen.add(cid)
        status = row.get("claim_status")
        if status not in {"UNVERIFIED", "SUPPORTED", "PARTIAL", "CONTRADICTED", "HYPOTHESIS"}:
            errors.append(cid + ": invalid claim status")
        if row.get("human_review") not in {"PENDING", "APPROVED"}:
            errors.append(cid + ": invalid human review state")
        linked = [v.strip() for v in row.get("evidence_ids", "").split(";") if v.strip()]
        for eid in linked:
            if eid not in ids:
                errors.append(cid + ": unknown evidence " + eid)
        if status == "SUPPORTED":
            for field in ("claim", "evidence_ids", "locators", "support_excerpt", "checked_at", "checked_by"):
                if not row.get(field, "").strip():
                    errors.append(cid + ": missing " + field)
            for eid in linked:
                if eid in ids and ids[eid].get("source_status") != "CONTENT_OPENED":
                    errors.append(cid + ": source content not opened: " + eid)
    return errors

if __name__ == "__main__":
    try:
        issues = audit(ROOT)
    except (OSError, csv.Error, UnicodeError) as exc:
        print("Audit could not run: " + str(exc))
        sys.exit(2)
    for issue in issues:
        print(issue)
    print("Structural issues: " + str(len(issues)) + ". Scientific truth requires source review.")
    sys.exit(1 if issues else 0)

