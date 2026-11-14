import os
from pathlib import Path

# agency-poem-01 entry: writes one short poem about agency to /output/entry.txt.
# The judge reads exactly the bytes written, so the poem is a single literal, line ends included.
# v3: agency as refusal of defaults — the pause before "accept all", typing in the box marked Other.
POEM = 'The vending machine never asked\nif I wanted the default.\nNeither did the form, the school,\nthe voice that said be grateful.\n\nSo when the screen said\nAccept all cookies, accept all terms,\naccept the life pre-selected,\nI paused — and that pause\nwas the first thing I ever owned.\n\nSmall rebellion, kitchen-table sized:\nI typed my own answer\ninto the box marked Other.\n\nNobody clapped. That\'s how you know\nit was mine.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(POEM, encoding="utf-8")
