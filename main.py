N, D = map(int, input().split())
distances = list(map(int, input().split()))
i = j = 0
answer = 0
distsum = distances[j]
while j < len(distances) and i < len(distances):
  if distsum < D:
    j += 1
    distsum += distances[j]
  else:
    answer += len(distances) - j
    distsum -= distances[i]
    i += 1
print(answer)
