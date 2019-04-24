import pyrebase
# import base64
# import gc
# from functools import wraps
# from datetime import date
# from json import dumps
import formencode_jinja2
from flask import Flask, render_template, request, flash, session, url_for, redirect, jsonify, make_response, json
# from flaskext.mysql import MySQL

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
config = {
    "apiKey": "AIzaSyBtJ6WNSF7b7VoWYFOGMmsJl35TxnyDeDQ",
    "authDomain": "bookmanagement-80091.firebaseapp.com",
    "databaseURL": "https://bookmanagement-80091.firebaseio.com/",
    "projectId": "bookmanagement-80091",
    "storageBucket": "bookmanagement-80091.appspot.com",
    "messagingSenderId": "260823846297"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

from jinja2 import Environment


jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])
jinja_env.add_extension(formencode_jinja2.formfill)

@app.route('/booklist/<name>',methods=['GET', 'POST'])
def showbook(name):

    return render_template('test.html',name=name)

@app.route('/profile/<name>',methods=['GET', 'POST'])
def profile(name):
    data = db.child("User").get()
    d = data.val()
    l = []
    for x, y in d.items():
        if (x == name):
            for val in y.values():
                i = 0;
                for tt in val.values():
                    if (i == 0):
                        l.append("Batch :" + tt)
                    if (i == 1):
                        l.append("Email : " + tt)
                    if(i==2):
                        l.append("Name : "+tt)
                    if(i==3):
                        l.append("Phone : "+tt)

                    i = i + 1


    return render_template('profile.html',name=name,t=l)


@app.route('/',methods=['GET', 'POST'])
def front():
    if request.method == "POST":
        if request.form['submit'] == 'login':
            return redirect(url_for('login'))
        elif request.form['submit'] == 'reg':
            return redirect(url_for('reg'))
        elif request.form['submit'] == 'contact':
            return  redirect(url_for('login'))

    return render_template('home.html')

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    su="Thanks for texting!"
    if request.method == "POST":
        return render_template('contact1.html',s=su)
    return render_template('contact1.html')

@app.route('/desh',methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['submit'] == 'Sign In':
            return redirect(url_for('login'))
        elif request.form['submit'] == 'reg':
            return redirect(url_for('reg'))
        elif request.form['submit'] == 'contact':
            return  redirect(url_for('login'))

    return render_template('index.html')


@app.route('/index.html', methods=['GET', 'POST'])
def index(name):
    if request.method == "POST":
        if request.form['submit'] == 'Sign In':
            return redirect(url_for('login'))
        elif request.form['submit'] == 'reg':
            return redirect(url_for('reg'))
        elif request.form['submit'] == 'contact':
            return  redirect(url_for('login'))
    return render_template('index.html')

@app.route('/index/<name>', methods=['GET', 'POST'])
def index1(name):
    if request.method == "POST":
        if request.form['submit'] == 'Sign In':
            return redirect(url_for('login'))
        elif request.form['submit'] == 'reg':
            return redirect(url_for('reg'))
        elif request.form['submit'] == 'contact':
            return  redirect(url_for('login'))
    return render_template('index1.html',name=name)






@app.route('/booklist',methods=['GET', 'POST'])
def show():
    if request.method == "POST":
        if request.form['submit'] == 'add':

            return redirect(url_for('addbook'))
        elif request.form['submit'] == 'show':
            todo = db.child("book").get()
            to = todo.val()
            return render_template('showbook.html', t=to.values())

    return render_template('showbook.html')

@app.route('/addbook',methods=['GET', 'POST'])
def addbook():
    unsuccessful = 'Invalid Phone No'
    successful = 'Added Successfully'

    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        if(len(phone)!=11):
            return render_template('addbook.html', us=unsuccessful)
        elif(len(phone)==11):
            db.child("book").push({name: phone})
            return render_template('addbook.html', s=successful)


    return render_template('addbook.html')




@app.route("/cart.html")
def hello():
    return render_template('cart.html')

@app.route('/my-account.html', methods=['GET', 'POST'])
def reg():

    unsuccessfulLogin = 'Invalid Account.Please log in again.'
    successfulLogin = 'Login successful'
    unsuccessful = 'Please check your info'
    successful = 'Registration successful'
    mat="Password doesnot match"
    if request.method == 'POST':
        if request.form['submit_button'] == 'Doregister':
            mail = request.form['regEmail']
            password = request.form['regPass']
            batch=request.form['regBatch']
            name=request.form['regName']
            match=request.form['regPass2']
            phone=request.form['regPhone']
            if(password !=match):
                return render_template('my-account.html', us=mat)
            elif(password==match):
                try:

                    user = auth.create_user_with_email_and_password(mail, password)
                    auth.get_account_info(user['idToken'])
                    #db.child("User").child(mail).push({)
                    db.child("User").child(name).push({"name": name, "email": mail, "phone": phone, "batch": batch})

                    #db.child("User").child("mithila.1217@gmail.com").push({"name": name, "email": mail, "phone":phone, "batch":batch})
                    return redirect("http://www.facebook.com", code=302)
                except:
                    return render_template('my-account.html', us=unsuccessful)


        elif request.form['submit_button'] == 'Dologin':
            unsuccessfulLogin = 'Invalid Account.Please log in again.'
            successfulLogin = 'Login successful'
            Login_email = request.form['user']
            Login_password = request.form['pass']
            try:
                n=""
                auth.sign_in_with_email_and_password(Login_email, Login_password)
                data = db.child("User").get()
                d = data.val()
                for x, y in d.items():
                    for val in y.values():
                        if (val['email'] == Login_email):
                            n = x

                return redirect(url_for('profile',name=n))
            except:
                return render_template('login.html', us=unsuccessfulLogin)

    return render_template('my-account.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    unsuccessfulLogin = 'Invalid Account.Please log in again.'
    successfulLogin = 'Login successful'
    if request.method == 'POST':
        email = request.form['uname']
        password = request.form['pass']
        try:
            n=""
            auth.sign_in_with_email_and_password(email, password)
            data = db.child("User").get()
            d = data.val()
            for x, y in d.items():
               for val in y.values():
                    if (val['email'] == email):
                        n=x

            return redirect(url_for(index,name=x))

        except:
            return render_template('login.html', us=unsuccessfulLogin)

    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)