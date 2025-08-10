import os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PROTECTED = [
  ROOT / "planning" / "master" / "coai_plan.md",
  ROOT / "planning" / "versions" / "coai_plan_v2.md",
  ROOT / "planning" / "progress" / "stage2" / "stage2_plan.md",
  ROOT / "planning" / "progress" / "stage3" / "stage3_plan.md",
]

def fail(msg):
  print("VALIDATION ERROR:", msg)
  sys.exit(1)

if __name__ == "__main__":
  for path in PROTECTED:
    if path.exists():
      txt = path.read_text(encoding="utf-8")
      if any(m in txt for m in ["[x]", "[v]", "[a]", "[!]"]):
        fail(f"Checkbox markers found in protected file: {path}")
  print("Validation OK.")
