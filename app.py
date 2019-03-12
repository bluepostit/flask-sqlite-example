from flask import Flask
from flask import render_template, request, url_for, redirect

import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/submit/", methods=['POST'])
def save_landmark():
    # 1. get data from request
    name_from_form = request.form.get('landmark')
    description_from_form = request.form['description']
    # 2. save it do the db
    data.add_landmark(name_from_form, description_from_form)
    return redirect(url_for('index'))
