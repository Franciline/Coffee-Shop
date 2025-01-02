from beverage_class import *
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
