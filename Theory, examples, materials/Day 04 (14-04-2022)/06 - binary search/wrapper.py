from time import perf_counter


def get_time(func):
  def wrapper(*args):
    start = perf_counter()
    res = func(*args)
    end = perf_counter()
    return res, '%.10f' % (end - start)
  return wrapper
