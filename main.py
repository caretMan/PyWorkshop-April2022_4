def put_percent_to_difference(difference):
    if int(difference) > 0:
        return f'+{difference}%'
    return f'{difference}%'


def difference_interpretation(difference):
    if int(difference) >= 50:
        return 'great'
    elif int(difference) >= 25:
        return 'decent'
    elif int(difference) >= 0:
        return 'need follow up'
    return ('critical')


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenues = [1500, 1000, 2000, 1800, 3000, 3900, 6500, 8000, 6500, 5900, 5400, 6000]
costs = [500, 100, 250, 1000, 340, 580, 670, 790, 600, 1200, 1500, 200]
profits = list(map(lambda x, y: x - y, revenues, costs))
raw_differences = ['%.d' % (profits[i] / profits[i - 1] * 100 - 100) for i in range(1, len(profits))]
differences = list(map(put_percent_to_difference, raw_differences))
interpretations = list(map(difference_interpretation, raw_differences))
differences = ['n/a'] + differences
interpretations = ['n/a'] + interpretations
for month, profit, difference, interpretation in zip(months, profits, differences, interpretations):
    print(f'{month} {profit} {difference} {interpretation}')