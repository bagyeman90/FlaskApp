""" 
This is a docstring for the main module.
"""

# Import the necessary modules
from flask import Flask

# Create the flask application now
app = Flask(__name__)

# Definf the routes for the application
@app.route('/')
@app.route('/index')
def index():
    """
    This is a docstring for the index function.
    Its parameters (if any), and its return value (if any).
    """
    return  '<p>Hello, World!</p>'
