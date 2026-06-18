from flask import Flask, render_template,request,redirect,url_for, flash, session
from database import get_products,get_sales,get_stock,insert_products,check_available_stock,insert_sales,check_user_exists,insert_user,sales_per_day, sales_per_product, profit_per_day, profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

#Flask Instance
app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Required for flashing messages definijg a secret key for the application to use flash messages
bcrypt = Bcrypt(app)

#index route
@app.route('/')
def home():
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def protected(*args, **kwargs):
        if 'email' not in session:
            flash("Please login to access this page", 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return protected


#products route
@app.route("/products")
# @login_required
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
        flash("product added successfully", 'success') 

    return redirect(url_for('products'))



#sales route
@app.route('/sales')
@login_required
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
            flash("Insufficient stock,add more", 'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale added successfully", 'success')
    return redirect(url_for('sales'))




#stock route
@app.route('/stock')
# @login_required
def stock():
    stock_data = get_stock()
    products = get_products()
    return render_template('stock.html',stock_data=stock_data,products=products)


@app.route('/dashboard')
@login_required
def dashboard():
    product_sales = sales_per_product()
    product_profit = profit_per_product()
    
    daily_sales = sales_per_day()
    daily_profit = profit_per_day()
    
    # 1. Product data for the dashboard charts
    products_name = [i[0] for i in product_sales]
    prod_profit = [float(i[1]) for i in product_profit]
    prod_sales = [float(i[1]) for i in product_sales]
    # 2. Time-series days data
    dates = [str(i[0]) for i in daily_sales]        
    days_sales = [float(i[1]) for i in daily_sales]       
    days_profit = [float(i[1]) for i in daily_profit]     
    
    return render_template(
        'dashboard.html',
        products_name=products_name,
        prod_profit=prod_profit,
        prod_sales=prod_sales,
        dates=dates,
        days_sales=days_sales,
        days_profit=days_profit
    )




@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            heshed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,heshed_password)
            insert_user(new_user)
            flash("Registration successful, you can now login", 'success')
            return redirect(url_for('login'))
        else:
            flash("User with this email already exists, please login", 'danger')
            return redirect(url_for('login'))



    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)

        if not registered_user:
            flash("User not found, please register", 'danger')
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1], password):
                session['email'] = email
                flash("Login successful", 'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid email or password", 'danger')
                return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash("You have been logged out", 'success')
    return redirect(url_for('login'))

#run your application
if __name__ == '__main__':
    app.run(debug=True)
