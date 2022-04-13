v1 = tuple(map(int, input().split()))
v2 = tuple(map(int, input().split()))
print(f'v1 = {v1} & v2 = {v2}')
for v1coord, v2coord in zip(v1, v2):
  print(v1coord + v2coord)