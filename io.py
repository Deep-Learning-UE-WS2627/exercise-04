
with open("wiki.txt", "r", encoding="utf-8") as file:
    sentences = file.readlines()

short_sentences = [sentence for sentence in sentences if len(sentence.strip()) < 30]

article_sentences = [
    sentence for sentence in sentences
    if sentence.startswith(("Der", "Die", "Das"))
]

april_sentences = [
    sentence for sentence in sentences
    if "April" in sentence
]

with open("short.txt", "w", encoding="utf-8") as file:
    file.writelines(short_sentences)

with open("articles.txt", "w", encoding="utf-8") as file:
    file.writelines(article_sentences)

with open("april.txt", "w", encoding="utf-8") as file:
    file.writelines(april_sentences)
