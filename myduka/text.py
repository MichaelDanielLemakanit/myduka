from database import get_products

product = get_products()
print(product)

for i in product:
    print(i[1])