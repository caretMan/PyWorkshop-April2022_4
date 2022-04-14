# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

a = 5
b = 2

print(a / b)  # work as expected


a = 5
b = 0

print(a / b)  # ZeroDivision

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

  
a = 5
b = 'five'

print(a / b)  # TypeError

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
except TypeError as err:
  print('T Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

# line num of exception
import sys 
e_type, e_object, e_traceback = sys.exc_info()
e_line = e_traceback.tb_lineno


# exception name
# use __class__.__name__ called on err object

# multiple exceptions
# except (ZeroDivisionError, TypeError) as err:
