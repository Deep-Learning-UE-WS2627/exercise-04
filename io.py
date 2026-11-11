
with open("wiki.txt", "r", encoding="utf-8") as file:
    sentences = file.read().splitlines()

short = [s for s in sentences if len(s) < 30]
articles = [s for s in sentences if s.startswith(("Der", "Die", "Das"))]
april = [s for s in sentences if "April" in s]

with open("short.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(short))

with open("articles.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(articles))

with open("april.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(april))
