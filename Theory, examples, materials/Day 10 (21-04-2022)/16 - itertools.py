import itertools

lst1, lst2, lst3 = [1, 2], [3, 4], [5, 6]

# chain

for num in itertools.chain(lst1, lst2, lst3):  # saves memory no obj created
  print(num)

# product

greets = ['Hi', 'Bye', 'Pls leave']
names = ['Anton', 'Greg']

for greet, name in itertools.product(greets, names):
  print(greet, name)

# product with repeat
  
chars = 'abcd1!'
low, high = (1, 4)

my_gen = (opt for i in range(low, high + 1) for opt in itertools.product(chars, repeat=i))
 
for opt in my_gen:
  print(''.join(opt))


# combinations

presents = ['p1', 'p2', 'p3', 'p4']

n = 3  # how many you can take from list of anything

my_gen = itertools.combinations(presents, 3)

for opt in my_gen:
  print('-'.join(opt))