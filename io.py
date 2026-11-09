with open("wiki.txt", "r", encoding="utf-8") as file:
    sentences = file.readlines()

short = [sentence for sentence in sentences if len(sentence.strip()) < 30]

articles = [sentence for sentence in sentences if sentence.startswith(("Der", "Die", "Das"))]

april = [sentence for sentence in sentences if "April" in sentence]

with open("short.txt", "w", encoding="utf-8") as file:
    file.writelines(short)

with open("articles.txt", "w", encoding="utf-8") as file:
    file.writelines(articles)

with open("april.txt", "w", encoding="utf-8") as file:
    file.writelines(april)