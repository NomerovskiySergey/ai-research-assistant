from pathlib import Path
import csv
import importlib.util
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

audit = load("audit").audit
export = load("export_mobile").export

class EvidenceChecks(unittest.TestCase):
    def fixture(self, root, opened="METADATA_MATCHED", linked="E001"):
        (root / "research").mkdir()
        source_fields = ["evidence_id", "source_status"]
        claim_fields = ["claim_id", "claim", "evidence_ids", "locators", "support_excerpt",
                        "claim_status", "checked_at", "checked_by", "human_review"]
        for name, fields, row in [
            ("sources", source_fields, ["E001", opened]),
            ("claims", claim_fields, ["C001", "Example proposition", linked, "p.2",
                                     "Example support", "SUPPORTED", "2026-10-09", "test", "PENDING"])]:
            with (root / "research" / (name + ".csv")).open("w", newline="", encoding="utf-8") as h:
                writer = csv.writer(h)
                writer.writerow(fields)
                writer.writerow(row)

    def test_metadata_does_not_support_claim(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            self.assertTrue(any("not opened" in e for e in audit(root)))

    def test_dangling_reference_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root, "CONTENT_OPENED", "E999")
            self.assertTrue(any("unknown evidence" in e for e in audit(root)))

    def test_opened_source_structural_pass(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root, "CONTENT_OPENED")
            self.assertEqual([], audit(root))

    def test_export_excludes_private_and_inbox(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for rel in load("export_mobile").ALLOWLIST + ["AGENTS.md", "docs/EVIDENCE.md",
                       "private/secret.txt", "inbox/return.md"]:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("SECRET" if rel.startswith(("private/", "inbox/")) else "PUBLIC", encoding="utf-8")
            export(root, "test-revision")
            for path in (root / "mobile").iterdir():
                self.assertNotIn("SECRET", path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()

