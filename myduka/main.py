from flask import Flask, render_template,request,redirect,url_for
from database import get_products,get_sales,get_stock,insert_products,check_available_stock,insert_sales

#Flask Instance
app = Flask(__name__)

#index route
@app.route('/')
def home():
    return render_template("index.html")


#products route
@app.route("/products")
def products():
    products_data = get_products()
    return render_template('products.html',products_data=products_data)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print("product added successfully") 

    return redirect(url_for('products'))



#sales route
@app.route('/sales')
def sales():
    sales_data = get_sales()
    products = get_products()
    return render_template('sales.html',sales_data=sales_data,products=products)



@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid,quantity)
        available_stock = check_available_stock(pid)

        if available_stock < float(quantity):
            print("Insufficient stock,add more")
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        print("Sale added successfully")
    return redirect(url_for('sales'))




#stock route
@app.route('/stock')
def stock():
    stock_data = get_stock()
    products = get_products()
    return render_template('stock.html',stock_data=stock_data,products=products)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')



#run your application
app.run(debug=True)