from random import randint
from string import ascii_lowercase
letters = [ascii_lowercase[randint(0, 25)] for _ in range(20)]
vowels = ['a', 'e', 'i', 'o', 'u']
def choose_vowels(letter):
  if letter in vowels:
    return(True)
print(list(filter(choose_vowels, letters)))