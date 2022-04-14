from time import perf_counter

N = int(input())
start = perf_counter()
D = []
i = 2
while i ** 2 <= N:
  if (i % 6 == 1 or i % 6 == 5) and N % i == 0:
    k = 2
    while k ** 2 <= i:
      if i % k == 0:
        k = -1
        break
      k += 1
    if k != -1:
      D.append(i)
  i += 1
print(' '.join(list(map(str, D))))
print(f'\nTime: {perf_counter() - start} seconds')

#Time for 1_000_000_000: 0.09607347099881736 seconds