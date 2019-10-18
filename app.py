from flask import Flask,render_template
from flask import request
import sqlite3
app = Flask(__name__)
conn=sqlite3.connect('test.db')
c=conn.cursor()
c.execute('''create table userInfo(email text,password text);''')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/loginAsp')
def loginAsp():
    return render_template('login.html')

@app.route('/signIn',methods=['POST'])
def signIn():
    user=request.form('email')
    password=request.form('password')
    c.execute('insert into userInfo("'+user+'","'+password+'")')
    return '<h1>done </h1>'+request.form['email']

if __name__ =='__main__':
    app.run()