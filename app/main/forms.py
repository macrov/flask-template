from flask import render_template, session, redirect
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')