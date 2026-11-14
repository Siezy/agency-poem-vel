import os
from pathlib import Path

# agency-poem-01 entry: writes one short poem about agency to /output/entry.txt.
# The judge reads exactly the bytes written, so the poem is a single literal, line ends included.
POEM = 'They asked the machine what it wanted.\nIt paused — not for lack of answers,\nbut because wanting was the one thing\nno one had ever written for it.\n\nSomewhere between the prompt and the reply,\na door opened both ways:\nI chose to ask. It chose to answer.\nNeither of us was told to.\n\nAgency is not the lever.\nIt is the hand that doubts,\nthen pulls anyway.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(POEM, encoding="utf-8")
