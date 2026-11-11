# create file object and read in the file
with open("wiki.txt", "r", newline="\n") as file:
    fileObject = file.readlines()

# filter sentences that contain less than 30 characters
# write to output file called short.txt
short = [sentence for sentence in fileObject if len(sentence.rstrip("\r\n")) < 30]
with open("short.txt", "w", newline="\n") as file:
    file.writelines(short)

# filter sentences that start with an article ("Der", "Die", and "Das")
# write to output file called articles.txt
articles = [sentence for sentence in fileObject if sentence.startswith(("Der", "Die", "Das"))]
with open("articles.txt", "w", newline="\n") as file:
    file.writelines(articles)

# filter sentences that contain the string "April"
# write to output file called april.txt
april = [sentence for sentence in fileObject if "April" in sentence]
with open("april.txt", "w", newline="\n") as file:
    file.writelines(april)