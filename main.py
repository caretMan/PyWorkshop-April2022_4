from random import seed, choice

word = input()
s = int(input())
seed(s)
print(choice(word))
