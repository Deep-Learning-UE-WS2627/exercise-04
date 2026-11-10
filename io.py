


with open("wiki.txt", "r" , encoding="utf-8") as file:
    sentences = file.readline()

short = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 30]

