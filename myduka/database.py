# import psycopg2
# #establishing a connection to a postgress db
# conn = psycopg2.connect(host='localhost', port=5432, user='postgres', password='2201', dbname='myduka')
# #cur object
# cur = conn.cursor()

# cur.execute("select * from products")
# products_data = cur.fetchall()
# print(products_data)

# #insert two records in sqlshell use psycopg2 to display them in your terminal

# # import psycopg2

# # # establishing a connection to a postgres db
# # conn = psycopg2.connect(host='localhost', port=5432, user='postgres', password='2201', dbname='myduka')

# # # cur object
# # cur = conn.cursor()

# # # 1. Insert a sale (assuming milk has an id of 1)
# # # We pass pid=1, quantity=5, and product_name='milk'
# # cur.execute("INSERT INTO sales (pid, quantity, product_name) VALUES (%s, %s, %s)", (1, 5, 'milk'))

# # # 2. IMPORTANT: Commit the changes to save them permanently
# # conn.commit()

# # print("Sale inserted successfully!")

# # 3. Read it back to verify
# cur.execute("SELECT * FROM sales")
# sales_data = cur.fetchall()
# print(sales_data)

# # # close connection
# # cur.close()
# # conn.close()

import psycopg2
#establishing a connection to a postgres db
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='2201',dbname='myduka')
 #cursor object
cur=conn.cursor()
def get_products():
    cur.execute('select * from products')
    products_data=cur.fetchall()
    return products_data

# cur.execute("insert into products(name,buying_price,selling_price)values('wallet',300,500)")
# conn.commit()
# print(products_data)

def get_sales():
    cur.execute('select * from sales')
    sales_data=cur.fetchall()
    return sales_data

def insert_products2(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1=('tissue',35,50)
product2=('valon',120,150)

insert_products2(product1)
insert_products2(product2)
products_data=insert_products2
print(products_data)

def insert_products2(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product3=('charger',200,350)
# insert_products2(product3)
products_data=insert_products2
print(products_data)
# Q1
def get_stocks():
    cur.execute("select * from stock")
    stocks_data = cur.fetchall()
    return stocks_data

stocks_data = get_stocks()
print(stocks_data)

#insert sales() 

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

sales1=(4,8)
sales2=(3,12)
sales3=(5,20)


insert_sales(sales1)
insert_sales(sales2)
insert_sales(sales3)


sales_data=get_sales()
print(sales_data)

# -> insert_stock()
def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",values)
    conn.commit()

stock1=(2,16)
stock2=(5,21)
stock3=(7,35)

insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)

stocks_data = get_stocks()
print(stocks_data)