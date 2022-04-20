random_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
word = input()
try:
  print(random_dict[word])
except KeyError:
  print('Not in the dictionary')
