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
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='2201',dbname='myduka')

#cur object
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data
    

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def get_stock():
    cur.execute("select * from stock")
    stock_data = cur.fetchall()
    return stock_data


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price, selling_price)values{values}")
    conn.commit()

product1 = ('shoes',2000,2500)
product2 = ('phone',10000,15000)

# insert_products(product1)
# insert_products(product2)


def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)", values)
    conn.commit()


def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)", values)
    conn.commit()


def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)", values)
    conn.commit()


product3 = ('laptop',40000,50000)
insert_products2(product3)


def sales_per_day():
    cur.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = cur.fetchall()
    return daily_sales


def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price -
        products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by date;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit



def sales_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)  as total_sales
        from products join sales on sales.pid = products.id group by p_name;
    """)
    product_sales = cur.fetchall()
    return product_sales


def profit_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity *( products.selling_price - 
        products.buying_price))  as total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    product_profit = cur.fetchall()
    return product_profit