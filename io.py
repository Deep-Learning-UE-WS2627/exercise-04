with open("wiki.txt", encoding="UTF-8") as file:
    text1 = file.read()

zeilen = text1.splitlines()

def unter30(zeilen, dateiname="short.txt"):
    kurze_zeilen = [zeile for zeile in zeilen if len(zeile) <= 30]

    with open(dateiname, mode="w", encoding="UTF-8") as file30:
        for zeile in kurze_zeilen:
            file30.write(zeile + "\n")

    return kurze_zeilen

unter30(zeilen)

def artikelSatze(zeilen, dateiname="article.txt"):
    artikel_zeilen = [zeile for zeile in zeilen if zeile.startswith('Die ') or zeile.startswith('Das ') or zeile.startswith('Die ')]

    with open(dateiname, mode="w", encoding="UTF-8") as fileArt:
        for zeile in artikel_zeilen:
            fileArt.write(zeile + "\n")

    return artikel_zeilen

artikelSatze(zeilen)

def aprilSatze(zeilen, dateiname="april.txt"):
    april_zeilen = [zeile for zeile in zeilen if "April" in zeile]

    with open(dateiname, mode="w", encoding="UTF-8") as fileApril:
        for zeile in april_zeilen:
            fileApril.write(zeile + "\n")

    return april_zeilen

aprilSatze(zeilen)

file.close()