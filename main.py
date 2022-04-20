def binary(Min_time, step):
  if Min_time < min(x, y):
    Copies = 0
    Copies1 = 0
  else:
    Copies = 1 + (Min_time - min(x, y)) // x + (Min_time - min(x, y)) // y
    if Min_time - 1 < min(x, y):
      Copies1 = 0
    else:
      Copies1 = 1 + (Min_time - 1 - min(x, y)) // x + (Min_time - 1 - min(x, y)) // y
  if step <= 1:
    step = 2
  if Copies >= N and Copies1 < N:
    return Min_time
  if Copies >= N:
    step = step // 2
    return binary(Min_time - step, step)
  if Copies < N:
    step = step // 2
    return binary(Min_time + step, step)

N, x, y = map(int, input().split())
print(binary(N // min(x, y), N // min(x, y)))
