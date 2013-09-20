import os
from flask import Flask, render_template, request
import sqlalchemy as sa

app = Flask(__name__)

app.debug = True

@app.route('/')
def root():
    return render_template('root.html', hello="hhhh")

@app.route('/boast', methods=['GET', 'POST'])
def boast():
    return request.args.get('brag')
    