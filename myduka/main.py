from flask import Flask, render_template,request,redirect,url_for,flash,session
from database import get_products,get_sales,get_stock,insert_products,check_available_stock,insert_sales,check_user_exists,create_user,sales_per_day,sales_per_product,profit_per_day,profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps 


#Flask Instance
app = Flask(__name__)

#Bcrypt instance with Flask app
bcrypt = Bcrypt(app)


app.secret_key = '78cbn88enhcucbhd99njsnns'

#index route
@app.route('/')
def home():
    return render_template("index.html")


def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


#products route
@app.route("/products")
@login_required
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
        flash("Product added successfully",'success') 

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
            flash("Insufficient stock,add more",'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))


#stock route
@app.route('/stock')
@login_required
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

    #product data
    product_names = [ i[0] for i in product_sales ]
    prod_profit = [ float(i[1]) for i in product_profit  ]
    prod_sales = [ float(i[1]) for i in product_sales ]


    #days data 
    dates = [ str(i[0]) for i in daily_sales ]
    day_sales = [ float(i[1]) for i in daily_sales ]
    day_profit = [ float(i[1]) for i in daily_profit ]

    return render_template('dashboard.html',
            product_names = product_names,prod_profit = prod_profit , prod_sales = prod_sales,
            dates = dates , day_sales = day_sales, day_profit = day_profit 
                           )


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            create_user(new_user)
            flash("User created successfully",'success')
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login instead",'danger')
        
    return render_template('register.html')




@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash("User doesn't exist,please register",'danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                session['email'] = email
                flash("Login successful",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect password,try again",'danger')
    
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("Logged out successfully",'success')
    return redirect(url_for('login'))




#run your application
app.run(debug=True)