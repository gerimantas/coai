import re, os, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGES = {
  "II":  ROOT / "planning" / "progress" / "stage2" / "stage2_plan_copy.md",
  "III": ROOT / "planning" / "progress" / "stage3" / "stage3_plan_copy.md",
}
DASHBOARD = ROOT / "planning" / "progress" / "coai_progress.md"
LOG = ROOT / ".coai" / "logs" / "progress_updates.log"

def parse_stats(path: Path):
  txt = path.read_text(encoding="utf-8") if path.exists() else ""
  total = len(re.findall(r"^\s*[-*]\s*\d+\.\d+\s*\[", txt, flags=re.M))
  done  = len(re.findall(r"\[x\]", txt, flags=re.I))
  ver   = len(re.findall(r"\[v\]", txt, flags=re.I))
  appr  = len(re.findall(r"\[a\]", txt, flags=re.I))
  block = len(re.findall(r"\[!\]", txt, flags=re.I))
  return dict(total=total, done=done, verified=ver, approved=appr, blocked=block)

def pct(d):
  denom = d["total"] or 1
  return round(100.0 * (d["done"] + d["verified"] + d["approved"]) / denom)

if __name__ == "__main__":
  stats = {k: parse_stats(v) for k, v in STAGES.items()}
  with DASHBOARD.open("w", encoding="utf-8") as f:
    f.write("# COAI Progress Dashboard\n\n")
    f.write(f"- Stage I: 100% (Completed)\n")
    f.write(f"- Stage II: {pct(stats['II'])}%\n")
    f.write(f"- Stage III: {pct(stats['III'])}%\n\n")
    f.write("## Links\n")
    f.write("- Stage II Working Copy: planning/progress/stage2/stage2_plan_copy.md\n")
    f.write("- Stage III Working Copy: planning/progress/stage3/stage3_plan_copy.md\n")
  LOG.parent.mkdir(parents=True, exist_ok=True)
  ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  with LOG.open("a", encoding="utf-8") as lf:
    lf.write(f"{ts} Updated dashboard: II={pct(stats['II'])}%, III={pct(stats['III'])}%\n")
