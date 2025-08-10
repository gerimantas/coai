import sys, os, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def usage():
  print("Usage: add_task.py <stage> <section> <title>")
  print("Example: add_task.py II 12 "Health check endpoint"")
  sys.exit(1)

def working_copy(stage: str) -> Path:
  stage_map = {"II": "stage2", "III": "stage3"}
  name = stage_map.get(stage.upper())
  if not name:
    sys.exit("Unknown stage. Use II or III.")
  return ROOT / "planning" / "progress" / name / f"{name}_plan_copy.md"

if __name__ == "__main__":
  if len(sys.argv) < 4: usage()
  stage, section, title = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
  path = working_copy(stage)
  if not path.exists():
    sys.exit(f"Working copy not found: {path}")
  lines = path.read_text(encoding="utf-8").splitlines()
  nums = []
  for ln in lines:
    s = ln.strip()
    if s.startswith(f"- {section}."):
      try:
        nums.append(int(s.split()[1].split('.')[1]))
      except Exception:
        pass
  n = (max(nums) + 1) if nums else 1
  now = datetime.datetime.now().strftime("%Y-%m-%d")
  lines.append(f"- {section}.{n} [ ] {title} (added {now}, ad-hoc)")
  path.write_text("\n".join(lines), encoding="utf-8")
  print(f"Added ad-hoc: {section}.{n} → {title}")
