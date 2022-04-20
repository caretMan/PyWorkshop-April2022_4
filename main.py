def binary(A, step):
  A_without_unlucky = A - A // 13 - A // 17 + A // (13 * 17)
  A1_without_unlucky = (A + 1) - (A + 1) // 13 - (A + 1) // 17 + (A + 1) // (13 * 17)
  if step == 0:
    step = 2
  if N >= A_without_unlucky and N < A1_without_unlucky:
    return A
  if N > A_without_unlucky:
    step = step // 2
    return binary(A + step, step)
  if N <= A1_without_unlucky:
    step = step // 2
    return binary(A - step, step)

N = int(input())
print(binary(3 * N // 2, N))