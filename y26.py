input_list = [line.split() for line in input('Enter the input >>> ').split('\n') if line]
input_splice = input_list.index(['Expenses'])
commissions = dict.fromkeys(input_list[1], 0)
revenues = {elem[0]: {name: int(revenue) for name, revenue in zip(input_list[1], elem[1:])} for elem in input_list[2: input_splice]}

for elem in input_list[input_splice + 2:]:
    for name, expense in zip(input_list[1], elem[1:]):
        commissions[name] += max(0, revenues[elem[0]][name] - int(expense))

print(' '12 + ' '.join(f'{key:>{max(len(key), len(str(val)))}}' for key, val in commissions.items()) + '\nCommission  ' + ' '.join(f'{str(round(val 0.062, 2)):>{max(len(key), len(str(val)))}}' for key, val in commissions.items()))

Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76
