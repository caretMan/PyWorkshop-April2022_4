# string decorator 1

def my_decor1(func):
  def wrapper(arg_for_func):
    print('It is amazing see you here!')
    return func(arg_for_func)
  return wrapper


@my_decor1
def greet(name):
  return f'Hello, {name}!!'

print(greet('John'))

# string decorator2

def my_decor2(func):
  def wrapper(*args_for_func):
    return ' '.join((func(*args_for_func), 'RUB'))
  return wrapper


@my_decor2
def calculate(a, b):
  return str(a // b)

print(calculate(1000, 25))