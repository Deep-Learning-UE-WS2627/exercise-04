import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

def func1():
  i = 0
  for outerlist in l1:
    print(i, end=" ")
    for element in outerlist:
      print(element, end=" ")
    print()
    i = i + 1

def func2():
  i = 0
  for outerlist in l1:
    print(i, end=" ")
    for j in range(20):
      try:
        print(f"{outerlist[j]:3}", end=" ")
      except IndexError:
        print(f"{0:3}", end=" ")
    print()
    i = i + 1

func2()
