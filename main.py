N, D = map(int, input().split())
weights = list(map(int, input().split()))
i, j = 0, 1
answer = 0
while j > i and len(weights) > 0:
  if j < len(weights) and weights[j] + weights[i] <= D:
    j += 1
  else:
    j -= 2
    if weights[j + 1] + weights[i] <= D:
      weights.pop(j + 1)
      weights.pop(i)
      if j >= len(weights):
        j -= 1
      answer += 1
    else:
      j += 1
answer += len(weights)
print(answer)
