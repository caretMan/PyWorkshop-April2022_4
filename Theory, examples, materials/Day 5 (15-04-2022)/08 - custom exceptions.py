# Custom Exceptions

# specifying message in arg
def example_exceptions_1(x, y):
  if y == 0:
    raise ZeroDivisionError('the dem is 0')
  elif y < 0:
    raise Exception('the dom is neg')
  else:
    print(x / y)

example_exceptions_1(10, 0)
example_exceptions_1(10, -1)


# raising with try/except
class NegativeResultException(Exception):
  pass
  
def example_exceptions_2(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')

example_exceptions_2(10, -1)

# raising several exceptions
class NegativeResultException(Exception):
  pass

class DenomOutOfBoundsException(Exception):
  pass
  
def example_exceptions_3(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    elif 1 < y < 10:
      raise DenomOutOfBoundsException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')
  except DenomOutOfBoundsException:
      print('denom can not be = from 2 to 9')

example_exceptions_3(10, -1)
example_exceptions_3(10, 4)

# by __str__ dunder
class OutOfBoundsException(Exception):
    def __str__(self):
      self.message = f'x can not be processed'
  

def example_exceptions_4(x):
    try:
        if 3 < x < 30:
            raise OutOfBoundsException
        else:
            print(x)
    except OutOfBoundsException as err:
        print(err)

example_exceptions_4(16)


# by __init__ dunder and parsing var to class
class NotInBoundException(Exception):
    def __init__(self, x):
      self.message = f'{x} can not be processed'
      super().__init__(self.message)


def example_exceptions_5(x):
    try:
        if 3 < x < 30:
            raise NotInBoundException(x)
        else:
            print(x)
    except NotInBoundException as err:
        print(err)

example_exceptions_5(10)
