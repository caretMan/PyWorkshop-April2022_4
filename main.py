from random import randint
Candidates = ['Денис', 'Дима', 'Ваня', 'Дима', 'Дима', 'Лёха', 'Вова', 'Вадим', 'Богдан', 'Юра', 'Антон', 'Артем', 'Костя']
Maths = [randint(25, 50) for _ in Candidates]
Physics = [randint(25, 50) for _ in Candidates]
English = [randint(25, 50) for _ in Candidates]
Results = list(map(lambda a, b, c, d: [a, b + c + d], Candidates, Maths, Physics, English))
def is_admitted(result):
  if int(result[1]) >= 100:
    return True
Admitted = list(filter(is_admitted, Results))
print(list(map(lambda x: x[0], Admitted)))
