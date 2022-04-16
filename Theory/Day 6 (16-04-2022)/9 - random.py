import random
from functools import reduce


letters  = [chr(n) for n in range(65, 80)]
freqs = [n + 1 for n in range(len(letters))][::-1]
print(letters)
print(freqs)


print(random.choices(letters, freqs))

password = [random.choices(letters, freqs) for _ in range(6)]
print(password)

print(''.join(reduce(lambda a, b: a + b, password)))
