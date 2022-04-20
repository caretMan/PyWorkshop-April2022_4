def binary(Step, Current):
  Sum, Sum1 = 0, 0
  for i in range(len(L)):
    Sum += L[i] // Current
  for i in range(len(L)):
    Sum1 += L[i] // (Current + 1)
  if Step <= 1:
    Step = 2
  if Sum >= K:
    if Sum1 < K:
      return Current
    Step = Step // 2
    return binary(Step, Current + Step)
  if Sum < K:
    Step = Step // 2
    return binary(Step, Current - Step)


N, K = map(int, input().split())
L = []
Ltotalsum = 0
for i in range(N):
  L.append(int(input()))
  Ltotalsum += L[-1]
Lmax = max(L)
Step = Lmax // 2
Current = max(L) // 2
if Ltotalsum >= K:
  print(binary(Step, Current))
else:
  print(0)
