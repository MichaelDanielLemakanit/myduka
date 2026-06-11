from flask import Flask,  render_template
from database import get_products, get_sales

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    number = 1000
    return render_template('index.html', x=number)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/products')
def products():
    products_data = get_products()  # Fetch products from the database
    return render_template('products.html', products_data = products_data)  # Pass products data to the template


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html', sales_data = sales_data)

@app.route('/stock')
def stock():
    return render_template('stock.html')

app.run()