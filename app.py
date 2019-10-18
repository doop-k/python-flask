from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/loginAsp')
def loginAsp():
    return render_template('login.html')

@app.route('/signIn',method=['POST'])
def signIn():
    user=request.form('email')
    password=request.form('password')

    return '<h1>done </h1>'+request.form['email']


if __name__ =='__main__':
    app.run()