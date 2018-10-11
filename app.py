import os

from flask import Flask
from flask import render_template, request
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def home():
    return render_template('calculatorTest.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)