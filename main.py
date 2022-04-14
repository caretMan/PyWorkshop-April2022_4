a = int(input())
b = int(input())
try:
  print('%.1f' % (a / b))
except ZeroDivisionError:
  print("The Error!")