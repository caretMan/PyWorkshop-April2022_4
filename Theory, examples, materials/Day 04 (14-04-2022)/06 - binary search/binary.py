from wrapper import get_time

@get_time
def binary(arr, low, high):
  i = 1
  while True:
    if arr[low] < arr[high]:
      return arr[high], i
    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
      return arr[mid], i
    if arr[mid] > arr[high]:
      low = mid + 1
    elif arr[mid] < arr[high]:
      high = mid - 1
    i += 1
  return None
