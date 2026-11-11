import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  for element in outerlist:
    print(element, end=" ")
  print()
  i = i + 1

  '''Padding mechanism, to change lines 8 + 9 to max length.
  Iterate over the list until 20, try accessing the element. If NULL throw exception + fill rest with 0s'''
def padding_mechanism(l):
  count = 0
  while count < 20:
    try:
      l.append(0)
      count += 1
    except IndexError:
      l.append(0)
      count += 1
  print("done")
padding_mechanism(l1)


