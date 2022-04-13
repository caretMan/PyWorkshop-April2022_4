# Tasks 1 - 3:
# (Работает для списков как с неповторяющимися, так и с повторяющимися числами)

from random import randint


def list_move(list: list):
  move = randint(0, len(list) - 1)
  return list[-move:] + list[:-move]


def binary_search_max(list:list):
    if len(list) < 2:
        return list[0]
    else:
        if list[0] > list[len(list) // 2]:
            MaxElement = binary_search_max(list[:len(list) // 2])
            return MaxElement
        else:
            MaxElement = binary_search_max(list[len(list) // 2:])
            return MaxElement


def binary_search_min(list:list):
    if len(list) < 2:
        return list[0]
    else:
        if list[len(list) // 2 - 1] <= list[-1]:
            MinElement = binary_search_min(list[:len(list) // 2])
            return MinElement
        else:
            MinElement = binary_search_min(list[len(list) // 2:])
            return MinElement


given_list = [randint(0, 1000) for _ in range(13)]
given_list.sort()
given_list = list_move(given_list)
print(given_list)
MaxElement = binary_search_max(given_list)
print(f'Max = {MaxElement}')
MinElement = binary_search_min(given_list)
print(f'Min = {MinElement}')

# Task 4: log(N)

# Task 5: нет

# Task 6: Разбиваем список на 2 равные части (или, в случае списка длиной 2n+1 нечетной длины, разбиваем его на 2 части длины n и n+1). Затем сравниваем первые элементы данных частей, и та часть, у которой первый элемент больше, и содержит в себе максимальный элемент. Если рассматриваемые первые элементы частей равны, то берем тот, который ближе к концу в исходном списке. Это работает, поскольку числа отсортированы (пусть и сдвинуты на рандомное число позиций), то есть относительно какого-либо числа перед тем, как будет максимум, числа будут исключительно возрастать; после максимума не может встретиться число, меньшее рассматриваемого.