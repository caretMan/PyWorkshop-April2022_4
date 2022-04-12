from random import randint


def is_positive(a):
  if a > 0:
    return True


def find_positive(my_list):
  return(list(filter(is_positive, my_list)))


my_list = [randint(-1000, 1000) for _ in range(25)]
print(f'{my_list}\n\n{find_positive(my_list)}')
