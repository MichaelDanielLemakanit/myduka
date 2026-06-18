import psycopg2

# Establishing a connection to a postgres db
conn = psycopg2.connect(host='localhost', port=5432, user='postgres', password='2201', dbname='myduka')

# Cursor object
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
    cur.execute("insert into products(name, buying_price, selling_price) values (%s, %s, %s)", values)
    conn.commit()

def insert_sales(values):
    cur.execute("insert into sales(pid, quantity) values (%s, %s)", values)
    conn.commit()

def insert_stock(values):
    cur.execute("insert into stock(pid, stock_quantity) values (%s, %s)", values)
    conn.commit()

# --- DATA VISUALIZATION FUNCTIONS ---

def sales_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as total_sales 
        from sales 
        join products on products.id = sales.pid 
        group by date order by date;
    """)
    daily_sales = cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity * (products.selling_price - products.buying_price)) as total_profit 
        from sales 
        join products on products.id = sales.pid 
        group by date order by date;
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        select products.name as p_name, sum(sales.quantity * products.selling_price) as total_sales
        from products 
        join sales on sales.pid = products.id 
        group by p_name;
    """)
    product_sales = cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
        select products.name as p_name, sum(sales.quantity * (products.selling_price - products.buying_price)) as total_profit 
        from products 
        join sales on sales.pid = products.id 
        group by p_name;
    """)
    product_profit = cur.fetchall()
    return product_profit

# --- AUTH & INVENTORY CHECKS ---

def check_available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid = %s", (pid,))
    stock_row = cur.fetchone()
    total_stock = stock_row[0] if stock_row and stock_row[0] is not None else 0

    cur.execute("select sum(sales.quantity) from sales where pid = %s", (pid,))
    sales_row = cur.fetchone()
    total_sold = sales_row[0] if sales_row and sales_row[0] is not None else 0

    return float(total_stock) - float(total_sold)

def check_user_exists(email):
    cur.execute("select * from users where email = %s", (email,))
    user = cur.fetchone()
    return user 

def insert_user(user_details):
    cur.execute("insert into users(full_name, email, phone_number, password) values (%s, %s, %s, %s)", user_details)
    conn.commit()