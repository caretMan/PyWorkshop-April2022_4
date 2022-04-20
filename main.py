def binary(A, t, l):
  if l == 0:
    l = 2
  if A >= t ** 2 and A < (t + 1) ** 2:
    return t
  if A > t ** 2:
    l = l // 2
    return binary(A, t + l, l)
  if A < t ** 2:
    l = l // 2
    return binary(A, t - l, l)


A = int(input())
print(binary(A, A // 2, A))