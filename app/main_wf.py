
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

# Create a SQLAlchemy object and bind it to the Flask app
db = SQLAlchemy(app)


# Define a model, which creates a table structure
class Product(db.Model):
    # Define the id column as an integer primary key
    id = db.Column(db.Integer, primary_key=True)
    # Define the product_name column as a string with a maximum length of 120 characters
    product_name = db.Column(db.String(120), nullable=False)
    # Define the price column as a float
    price = db.Column(db.Float, nullable=False)

    # Define a string representation for the Product class
    def __repr__(self):
        return '<Product %r>' % self.product_name



ALLOWED_EXTENSIONS = {'csv'}


# Check if the file extension is allowed
def allowed_file(filename):
    # Split the filename into its name and extension
    # Check if the extension is in the list of allowed extensions
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Process the file by reading its contents and adding records to the database
def process_file(file):
    # Read the file as a CSV using pandas
    df = pd.read_csv(file)
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Create a new record using the values from the row
        new_record = Product(product_name=row['product_name'], price=row['price'])
        # Add the new record to the database session
        db.session.add(new_record)
    # Commit the changes to the database
    db.session.commit()


# Define a route for the index page, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index3():
    message = ""  # Optional, for showing a message after upload

    # Check if the HTTP request method is 'POST'
    if request.method == 'POST':
        # Retrieve the file from the request
        file = request.files['file']
        # Check if the file is allowed based on its filename extension
        if file and allowed_file(file.filename):
            # Process the file by reading its contents and adding records to the database
            process_file(file)
            # Set a success message to be displayed
            message = "File uploaded successfully!"

    # Retrieve all products from the database
    products = Product.query.all()

    # Render the index3.html template, passing the products and message variables
    return render_template('index3.html', products=products, message=message)



if __name__ == '__main__':
    with app.app_context():
        print("Creating database...")
        db.create_all()
        print("Database created.")
    app.run(port=5001)


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index3():
#     # This will simply render the index3.html template without any additional data
#     return render_template('index3.html')

# # @app.route('/')
# # def index():
# #     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(port=5001)