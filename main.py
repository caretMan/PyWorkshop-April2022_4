from random import seed, shuffle

Words = input().split()
seed(43)
shuffle(Words)
print(' '.join(Words))