# linear search

lst = [1, 3, 6, 8, 9, 12, 13, 19]
num = 0
k = 1
for i in range(len(lst)):
  for j in range(i, len(lst)):
    if lst[j] - lst[i] >= 3:
      num += 1
      print(lst[i], lst[j])
    k += 1

print(num, k)


# two pointer search

i = j = 0
num = 0
k = 1
while i < len(lst) and j < len(lst):
  if lst[j] - lst[i] < 3:
    j += 1
  else:
    num += len(lst) - j
    i += 1
  k += 1
print(num, k)
