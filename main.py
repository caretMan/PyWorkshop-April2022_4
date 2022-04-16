class NegativeSumError(Exception):
    def __str__(self):
        return 'Error!'

def sum_with_exceptions(a, b):
    if a + b < 0:
        raise NegativeSumError
    else:
        return a + b

a, b = int(input()), int(input())
print(sum_with_exceptions(a, b))
