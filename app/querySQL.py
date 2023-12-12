from main_wf import app
from main_wf import db  # Replace 'your_flask_app' with the name of your Flask app file
from main_wf import Product  # Make sure Product class is accessible

# Query the database
with app.app_context():
    products = Product.query.all()

# Print the results
for product in products:
    print(f"ID: {product.id}, Name: {product.product_name}, Price: {product.price}")