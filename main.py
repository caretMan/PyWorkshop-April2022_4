class NotInBoundsError(Exception):
  def __str__(self):
    return 'There is an error!'


def check_integer(num):
  if 45 <= num <= 67:
    return num
  else:
    raise NotInBoundsError


def error_handling(num):
  try:
    check_integer(num)
  except NotInBoundsError as err:
    print(err)
  else:
    print(num)


num = int(input())
error_handling(num)