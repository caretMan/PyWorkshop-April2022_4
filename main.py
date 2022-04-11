Str = input()
if Str[0:len(Str) // 2] == Str[-1:(len(Str) + 1) // 2 - 1:-1]:
  print('Yes')
else:
  print('No')