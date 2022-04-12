Part1, Part2 = input(), input()
P1letters = [Part1[i] for i in range(len(Part1))]
P2letters = [Part2[i] for i in range(len(Part2))]
Name = ''
for P1letter, P2letter in zip(P1letters, P2letters):
  Name = f'{Name}{P1letter}{P2letter}'
print(Name)