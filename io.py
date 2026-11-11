with open("wiki.txt", encoding="UTF-8") as f:
    sentences = [line.strip() for line in f.readlines()]

short = [s for s in sentences if len(s) < 30]
articles = [s for s in sentences if s.startswith(("Der ", "Die ", "Das "))]
april = [s for s in sentences if "April" in s]

def write_lines(filename, lines):
    with open(filename, "w", encoding="UTF-8") as out:
        out.write("\n".join(lines) + "\n")

write_lines("short.txt", short)
write_lines("articles.txt", articles)
write_lines("april.txt", april)