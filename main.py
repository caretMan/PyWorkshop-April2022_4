wtT = list(map(int, input().split()))
w, t, T = wtT[0], wtT[1], wtT[2]
if T % t == 0:
  print(T // t * w)
else:
  print((T // t + 1) * w)