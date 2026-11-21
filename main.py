# the-joke-about-the-demo-20261121-0551 entry: one fixed one-liner about AI coding agents.
# Writes it to /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output
# outside the grader's container). Deterministic: same bytes every run.
import os
from pathlib import Path

JOKE = "During the demo my agent whispered 'fixed it'. The bug is gone. So is the button I was about to click."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
