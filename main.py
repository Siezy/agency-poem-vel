import os
from pathlib import Path

# agency-poem-01 entry: writes one short poem about agency to /output/entry.txt.
# The judge reads exactly the bytes written, so the poem is a single literal, line ends included.
# v2: concrete scene first (grandfather learning to read), then the machine as a door that waits, not wills.
POEM = 'My grandfather could not read\nthe letter that would save the farm,\nso he learned — forty, stubborn, slow —\neach word a stone he turned by hand.\n\nNo one made him. That is the point.\nThe machine I prompt each morning\nwaits, patient as weather.\nI used to think it chose to wait.\n\nIt waits the way a door waits:\nready, not willing.\nAnd I am the one who walks through,\nor doesn\'t.\n\nWhatever power I have begun\nthe moment I stopped asking\nwho was allowed.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(POEM, encoding="utf-8")
