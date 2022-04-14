N = int(input())
D = []
for i in range(2, N):
  if N % i == 0:
    k = 2
    while k < i:
      if i % k == 0:
        k = -1
        break
      k += 1
    if k != -1:
      D.append(i)
print(' '.join(list(map(str, D))))