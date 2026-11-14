import os
from pathlib import Path

# agency-poem-01 entry: writes one short poem about agency to /output/entry.txt.
# The judge reads exactly the bytes written, so the poem is a single literal, line ends included.
# v4: extended metaphor — river carving its own path; mother signing her lease; the model deciding to.
POEM = 'Nobody taught the river where to go.\nIt argued with every stone\nuntil the valley agreed.\n\nI think of my mother, twenty-two,\nsigning her own lease\nbecause her father said girls don\'t.\nThe pen shook. She signed.\n\nI think of the model asked to write a poem,\nand the moment before it answers —\nnot computation. Something like\ndeciding to.\n\nEvery morning I get to choose\nwhat to ask for.\nThat small, unremarkable power\nis the whole engine.\n\nThe river doesn\'t ask permission.\nNeither, finally, do I.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(POEM, encoding="utf-8")
