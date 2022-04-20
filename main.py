with open('summers and other things.txt', 'r', encoding='utf-8') as file:
  strs = file.readlines()
  print(strs)
  summers = strs.count('summer\n') + strs.count('summer')
  print(summers)
