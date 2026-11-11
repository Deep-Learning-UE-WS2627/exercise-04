import random

# Your padding implementation should use exceptions and only change lines 8 and 9. 
# The idea is to make a for loop until 20, and try to access the list element at the position. 
# If the list is shorter, we catch the exception and print a zero.

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  for element in range(20):
    try:
      print(outerlist[element], end=" ")
    except IndexError:
      print(0, end=" ")
  print()
  i = i + 1