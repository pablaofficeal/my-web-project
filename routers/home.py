from flask import Blueprint, render_template

home_host = Blueprint('home_host', __name__)

@home_host.route('/')
def index():
    return render_template('index.html')