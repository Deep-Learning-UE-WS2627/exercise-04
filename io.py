wikiContent = open("wiki.txt", encoding='utf-8')

wikiline = wikiContent.readlines()

sf = open('short.txt', mode="w", encoding='utf-8')
shorty = [sf.write(shortLine) for shortLine in wikiline if len(shortLine)<30]

ar = open('articles.txt', mode="w", encoding='utf-8') 
articly = [ar.write(articleLine) for articleLine in wikiline if articleLine.startswith(('Der', 'Die', 'Das'))]

af = open('april.txt', mode="w", encoding='utf-8')
aprily = [af.write(aprilLine) for aprilLine in wikiline if 'April' in aprilLine]


#print(shorty)
#print(articly)
#print(aprily)
wikiContent.close()
sf.close()
ar.close()
af.close()