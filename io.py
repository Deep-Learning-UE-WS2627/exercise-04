"""Filter Wikipedia sentences into three text files."""

from pathlib import Path


directory = Path(__file__).resolve().parent
with (directory / "wiki.txt").open(encoding="utf-8") as source:
    sentences = source.readlines()

short_sentences = [sentence for sentence in sentences if len(sentence.rstrip("\r\n")) < 30]
article_sentences = [sentence for sentence in sentences if sentence.startswith(("Der", "Die", "Das"))]
april_sentences = [sentence for sentence in sentences if "April" in sentence]

for filename, selected in (
    ("short.txt", short_sentences),
    ("articles.txt", article_sentences),
    ("april.txt", april_sentences),
):
    with (directory / filename).open("w", encoding="utf-8") as output:
        output.writelines(selected)
