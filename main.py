from flask import Flask

""" 
This is a docstring for the main module.
It describes what the module does.
"""
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """
    This is a docstring for the index function.
    Its parameters (if any), and its return value (if any).
    """
    return  '<p>Hello, World!</p>'
