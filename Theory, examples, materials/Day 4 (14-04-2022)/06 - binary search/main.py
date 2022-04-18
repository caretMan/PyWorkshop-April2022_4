from linear import linear
from binary import binary
from random import randint as rr


n = 10_000
array = [n for n in range(n + 1)]


def rotate(array):
  for _ in range(rr(1, len(array))):
    array.append(array.pop(0))
  return array

array = rotate(array)

print(linear(array))
print(binary(array, 0, len(array) - 1))
