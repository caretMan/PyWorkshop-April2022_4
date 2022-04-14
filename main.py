from time import perf_counter

N = int(input())
start = perf_counter()
D = []
i = 1
while i ** 2 <= N:
  if N % i == 0:
    D.append(i)
    D.append(N // i)
  i += 1
D.sort()
print(' '.join(list(map(str, D))))
print(f'\nTime: {perf_counter() - start} seconds')

#Time for 1_000_000_000: 0.04504243600058544 seconds