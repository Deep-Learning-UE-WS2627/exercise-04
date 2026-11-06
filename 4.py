import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0

#Das Außengehäuse, also da, wo noch keine Zahlen stehen
for outerlist in l1:
  print(i, end=" ")

  #Der Teil, in dem Zahlen stehen
  for element in outerlist:
    print(element, end=" ")
    #checkt, ob die Längenabfrage der inneren Liste aktiviert werden soll 
  if i == 8 or i == 9:
    try:
      for counter in range(20):
        outerlist[counter]
    except IndexError:
      for pups in range(20-counter):
        print(0, end="  ")
      

  #zusätzlicher Print, um neue Zeile zu schreiben, da die anderen Prints keine neue Zeile schreiben wollen, ist der hier notwendig
  print()
  i = i + 1