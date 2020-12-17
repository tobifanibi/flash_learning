# app.py

# Import the Flask class
from flask import Flask

# Starts a new Flask app using this app file
app = Flask(__name__)

# Start a new route for the index page
@app.route('/')
def index():
	return "Hello team penguin"

# When app is run, start the Flask app on the localhost server (port 5000)
if __name__ == "__main__":
	app.run(debug=True)