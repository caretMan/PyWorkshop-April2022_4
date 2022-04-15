import sys

try:
  a = int(input())
  b = int(input())
  c = int(input())
  if c == 1:
    print(d)
  else:
    print('%.2f' % (a / b))
except (NameError, ValueError, ZeroDivisionError) as err:
  err_type, err_object, err_traceback = sys.exc_info()
  err_line = err_traceback.tb_lineno
  print(f'{err.__class__.__name__} exception on line {err_line}!')
