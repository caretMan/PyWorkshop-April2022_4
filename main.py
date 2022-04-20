with open('sums.txt', 'r', encoding='utf-8') as file:
  for line in file:
    a, b = map(int, line.strip().split())
    print(a + b)