# map / takes a func

# -----------
nums = [n for n in range(10)]
double_nums = [n * 2 for n in nums]
print(nums)
print(double_nums)

# -----------
def doubler(x):
  return x * 2

double_numbers = list(map(doubler, nums))
print(double_numbers)

# -----------
a, b = map(int, (input(), input()))
print(a, type(a), b, type(b))

# -----------
double_numbers = list(map(lambda x: x * 2, nums))
print(double_numbers)

# -----------
x_list = [1, 2, 4]
y_list = [4, 6, 8]
z_list = [9, 10, 10]

res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)


#filter / takes a Boolean func (True or False)
odd_numbers = [n for n in nums if n % 2]
print(odd_numbers)

# -----------
odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)

#--------------------------------------------------
# map and filter can be replaced with list comprehention
# which is more PYTHONIC yet
# map and filter are generally more efficient and faster
