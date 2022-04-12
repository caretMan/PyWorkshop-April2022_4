def celsius_to_fahrenheit(temp_c):
  return('%.1f' % (9 / 5 * temp_c + 32))

def is_above_80(temp_f):
  if  float(temp_f) >= 80:
    return True


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))
print(daily_temp_f)

daily_temp_f_above_80 = list(filter(is_above_80, daily_temp_f))
print(f'\n{len(daily_temp_f_above_80)}')