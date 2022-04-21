from wrapper import get_time

@get_time
def linear(arr):
  i = 1
  for num in arr:
    i += 1
    if num > arr[arr.index(num) + 1]:
      return num, i
    return None
