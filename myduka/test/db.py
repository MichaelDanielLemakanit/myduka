from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2201@localhost:5432/myduka'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    all_products = Item.query.all()
    return render_template('index.html', products=all_products)

# This path MUST match your HTML form action exactly!
@app.route('/add-item', methods=['POST'])
def add_item():
    # 1. Capture the data from the frontend form
    form_name = request.form['product_name']
    form_price = request.form['product_price']
    
    # 💡 CONFIRMATION 1: Print to terminal what the user typed
    print(f"\n[BACKEND] 📥 Received new product form submission!")
    print(f"[BACKEND] Trying to save Name: '{form_name}' | Price: KSh {form_price}")
    
    # 2. Package it and save to PostgreSQL
    new_item = Item(name=form_name, price=int(form_price))
    db.session.add(new_item)
    db.session.commit()
    
    # 💡 CONFIRMATION 2: Print the assigned unique database ID
    print(f"[BACKEND] 🎉 SUCCESS! Saved to Postgres with generated Database ID: {new_item.id}\n")
    
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)