from database import sales_per_day

data = sales_per_day()
print(data)

# [('samsung phone', Decimal('96600000.00')), ('bread', Decimal('53800.00'))]

names = [i[0] for i in data]
print(names)