# generators

def multiples(a, n):
  i = 1
  result = []
  while i <= n:
    result.append(a * i)
    i += 1
  return result  # list


print(multiples(3, 5))  # gives whole list
print(multiples(2, 10))  # # gives whole list


def multiples(a, n):
  i = 1
  while i <= n:
    yield a * i  # yield is used instead of return to make results one by one
    i += 1

my_gen = multiples(3, 5)  # generator object
print(next(my_gen))  # gives 1st result
print(next(my_gen))  # gives 2nd result
print(next(my_gen))  # gives 3d result


numbers = [1, 2, 3]
my_generator = (n ** 2 for n in numbers)  # generator object
print(next(my_generator))  # gives 1st result
print(next(my_generator))  # gives 2nd result
print(next(my_generator))  # gives 3d result
print(next(my_generator))  # StopIteration Exception

for n in my_generator:  # can be used with for loop 
  print(n)
