N = int(input())
D = []
for i in range(1, N):
  if N % i == 0:
    D.append(i)
print(' '.join(list(map(str, D))))