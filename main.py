N, D = map(int, input().split())
coords = list(map(int, input().split()))
i = j = 0
answer = 0
while i < len(coords) and j < len(coords):
  if coords[j] - coords[i] < D:
    j += 1
  else:
    answer += len(coords) - j
    i += 1
print(answer)
