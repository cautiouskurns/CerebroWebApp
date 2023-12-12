
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'TestDatabase.db')

# Create a SQLAlchemy object and bind it to the Flask app
db = SQLAlchemy(app)


# Define models, which creates table structures
class Subject(db.Model):
    __tablename__ = 'subjects'
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(255), nullable=False)
    topics = db.relationship('Topic', backref='subject', lazy=True)

class Topic(db.Model):
    __tablename__ = 'topics'
    topic_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(255), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'), nullable=False)
    concepts = db.relationship('Concept', backref='topic', lazy=True)

class Concept(db.Model):
    __tablename__ = 'concepts'
    concept_id = db.Column(db.Integer, primary_key=True)
    concept_name = db.Column(db.String(255), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.topic_id'), nullable=False)



ALLOWED_EXTENSIONS = {'csv'}


# Check if the file extension is allowed
def allowed_file(filename):
    # Split the filename into its name and extension
    # Check if the extension is in the list of allowed extensions
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_file(file):
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        # Assuming your CSV has columns 'subject_name', 'topic_name', 'concept_name'
        subject = Subject.query.filter_by(subject_name=row['subject_name']).first()
        if not subject:
            subject = Subject(subject_name=row['subject_name'])
            db.session.add(subject)

        topic = Topic.query.filter_by(topic_name=row['topic_name'], subject=subject).first()
        if not topic:
            topic = Topic(topic_name=row['topic_name'], subject=subject)
            db.session.add(topic)

        concept = Concept(concept_name=row['concept_name'], topic=topic)
        db.session.add(concept)

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
    subjects = Subject.query.all()

    # Render the index3.html template, passing the products and message variables
    return render_template('index3.html', subjects=subjects, message=message)
    # return render_template('LearningDataOutputTest.html', subjects=subjects, message=message)


if __name__ == '__main__':
    with app.app_context():
        print("Creating database...")
        db.create_all()
        print("Database created.")
    app.run(port=5001)

