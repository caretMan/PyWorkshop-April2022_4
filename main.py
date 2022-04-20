def binary(A, step):
  if step == 0:
    step = 2
  if N >= A ** 3 and N < (A + 1) ** 3:
    return A
  if N > A ** 3:
    step = step // 2
    return binary(A + step, step)
  if N < A ** 3:
    step = step // 2
    return binary(A - step, step)


N = int(input())
print(binary(N // 2, N))
