from random import randint

dices = []
while dices != [5, 5] and dices != [6, 6]:
  dices = [randint(1, 6) for _ in range(2)]
print(' '.join(list(map(str, dices))))