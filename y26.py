def parse_input(sales_input):
    data = inp.split("\n\n")    
    sales = {data[0].strip(): data[1], data[2].strip(): data[3]}
    for k, v in sales.items():
        rows = [[elem.strip() for elem in r.split()]
                for r in v.splitlines()]
        df = pd.DataFrame(rows[1:])
        df.set_index(0, inplace=True)
        df.columns = rows[0]
        df = df.apply(pd.to_numeric)
        sales[k] = df
    return sales

def get_commission(sales_data):
    profit = sales["Revenue"] - sales["Expenses"]
    commission = profit*.062
    commission[commission < 0] = 0
    commission = commission.sum()
    return pd.DataFrame({"Commission": commission}).transpose()

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
Milk             67     254      89    129       76''')