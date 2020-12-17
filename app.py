# app.py

# Import the Flask class (for the main app)
# Import render_templates to run routes based on templates
# Import url_for in order to link stylesheets in the base jinja2 template
from flask import Flask, render_template, url_for

# Import SQLAlchemy to use backend database
from flask_sqlalchemy import SQLAlchemy

# imported to track date of creation of flashcards
from datetime import datetime


# Starts a new Flask app using this app file
app = Flask(__name__)

# Add config file specific for the database location (test db)
# This uses SQL Lite which is a very simple database with no frills
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Add additional config file to stop tracking modifications to SQL Alchemy, this isn't necessary, but removes a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the settings used in our app
db = SQLAlchemy(app)


# Create a model for a Flashcard
class Flashcard(db.Model):

	# Add a primary key with a id field
	id = db.Column(db.Integer, primary_key=True)

	# Add a column to the database with the string of the front side of our card
	content_front_side = db.Column(db.String(200), nullable=False)

	# Add a column to the database with the string of the back side of our card
	content_back_side = db.Column(db.String(200), nullable=False)

	# Add date of creation for bookeeping, with a default creation time of whenever it was created
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	# Add a repprint function just to make it easier to reference this flashcard
	def __repr__(self):
		return '<Flashcard %r>' % self.id

# Start a new route for the index page
@app.route('/')
def index():

	# User render templates to use the index.html file as a template for the index page
	return render_template('index.html')

# When app is run, start the Flask app on the localhost server (port 5000)
if __name__ == "__main__":
	app.run(debug=True)