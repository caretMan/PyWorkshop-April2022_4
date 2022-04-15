try:
  r = 5 // 0
except ZeroDivisionError:
  print('Error!')
else:
  print(f'Result = {r}')
finally:
  print('Thank you for using this program')