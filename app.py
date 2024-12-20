from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = "windill"):
    return render_template('hello.html', person=name)