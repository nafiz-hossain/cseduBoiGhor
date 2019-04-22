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
# from ClassLabRequest import ClassBookingReq,User,LabBookingReq
# from AudiFieldRequest import AuditoriumBookingReq,FieldBookingReq
# from Update import *
# from ClassLabBook import *
# from Signup import *
# from Auditorium import *
# from Field import *
# from Login import *
# from Profile import *
# from Pass import DB_PASS
#

jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])
jinja_env.add_extension(formencode_jinja2.formfill)
#
#
# app = Flask(__name__)
# mysql = MySQL()
# app.jinja_env.add_extension('jinja2.ext.loopcontrols')
# app.secret_key = "super secret key"
# app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# # app.config['MYSQL_DATABASE_PASSWORD'] = '$huvo919671'
# # app.config['MYSQL_DATABASE_DB'] = "Du_Booking_Data"
# app.config['MYSQL_DATABASE_PASSWORD'] = DB_PASS
# app.config['MYSQL_DATABASE_DB'] = "Booking_system"
# mysql.init_app(app)
#
# username = "Guest"
#
@app.route('/',methods=['GET', 'POST'])
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
def index():
    if request.method == "POST":
        if request.form['submit'] == 'Sign In':
            return redirect(url_for('login'))
        elif request.form['submit'] == 'reg':
            return redirect(url_for('reg'))
        elif request.form['submit'] == 'contact':
            return  redirect(url_for('login'))
    return render_template('index.html')






@app.route('/booklist',methods=['GET', 'POST'])
def showbook():
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






#
# @app.route('/index')
# def home():
#     return render_template('index.html')
#
# @app.route('/admin')
# def admin():
#     return render_template('admin.html')
#

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
            match=request.form['regPass2']
            if(password !=match):
                return render_template('my-account.html', us=mat)
            elif(password==match):
                try:
                    user = auth.create_user_with_email_and_password(mail, password)
                    auth.get_account_info(user['idToken'])

                    return redirect("http://www.facebook.com", code=302)
                except:
                    return render_template('my-account.html', us=unsuccessful)


        elif request.form['submit_button'] == 'Dologin':
            unsuccessfulLogin = 'Invalid Account.Please log in again.'
            successfulLogin = 'Login successful'
            Login_email = request.form['user']
            Login_password = request.form['pass']
            try:
                auth.sign_in_with_email_and_password(Login_email, Login_password)

                return redirect("http://www.youtube.com", code=303)
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
            auth.sign_in_with_email_and_password(email, password)

            return redirect("http://www.youtube.com", code=302)

        except:
            return render_template('login.html', us=unsuccessfulLogin)

    return render_template('login.html')



# @app.route('/signup_helper', methods=["GET", "POST"])
# def signup_helper():
#     return Signup_Class(mysql).signup_helper()

#
# @app.route('/login_helper', methods=["GET", "POST"])
# def login_helper():
#    return Login_Class(mysql).login_helper()
# #This is only for user before booking
# @app.route('/login_user', methods=["GET", "POST"])
# def login_user():
#     return Login_Class(mysql).login_user()
#
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             return redirect(url_for('login'))
#
#     return wrap
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     session.clear()
#     gc.collect()
#     return render_template("index.html")
# #Auditorium info page
# @app.route('/Auditorium_Blog',methods=["GET", "POST"])
# def blog1():
#     return render_template('Auditorium_Blog.html')
# #Field info page
# @app.route('/field_blog',methods=["GET", "POST"])
# def blog2():
#     return render_template('field_blog.html')
#
#
#
# #Start of auditorium
# #Here are all function of auditorium related
# @app.route('/auditorium_main',methods=['GET'])
# def auditorium_final():
#    return auditorium_book_class(mysql).auditorium_final()
#
# #After selecting date this function return data
# @app.route('/auditorium_data_query',methods=["GET","POST"])
# def auditorium_query():
#    return auditorium_book_class(mysql).auditorium_query()
#
# #this function receive auditorium name
# @app.route('/auditorium_book_helper',methods=["GET","POST"])
# def auditorium_book_helper():
#     return auditorium_book_class(mysql).auditorium_book_helper()
#
# @app.route('/auditorium_book',methods=["GET","POST"])
# def auditorium_book():
#    return auditorium_book_class(mysql).auditorium_book()
#
# # Start of fielding booking
# #Here are all function related to field booking
#
# @app.route('/field_main',methods=['GET'])
# def field_final():
#     return field_class(mysql).field_final()
# @app.route('/field_data_query',methods=["GET","POST"])
# def field_query():
#    return field_class(mysql).field_query()
#
# @app.route('/field_book_helper',methods=["GET","POST"])
# def field_book_helper():
#    return field_class(mysql).field_book_helper()
#
# @app.route('/field_book',methods=["GET","POST"])
# def field_book():
#    return field_class(mysql).field_book()
#
# @app.route('/user_profile',methods=["GET","POST"])
# def view_profile():
#     return profile_class(mysql).view_profile()
#
# @app.route('/ClassBookingReq',methods=['GET'])
# #initial page for booking requests this will show
# #all request for class booking
# def class_booking():
#     return ClassBookingReq(mysql).class_booking()
#
# @app.route('/table_clicked',methods=['GET'])
# #send user details information when a request button is clicked
# def row_clicked():
#     return User(mysql).row_clicked()
#
# @app.route('/user_image',methods=['GET','POST'])
# #send user image to admin
# def send_image():
#     return User(mysql).send_image()
#
# @app.route('/confirmation',methods=['GET','POST'])
# #admin confirmations or discarding information will be
# #sent to user through email
# def feedback():
#     return ClassBookingReq(mysql).feedback()
#
# #Lab booking request
# @app.route('/LabBookingReq',methods=['GET'])
# #page for booking requests this will show
# #all request for lab booking
# def lab_booking():
#     return LabBookingReq(mysql).lab_booking()
#
# @app.route('/lab_confirmation',methods=['GET','POST'])
# #admin confirmations or discarding information will be
# #sent to user through email
# def lab_feedback():
#     return LabBookingReq(mysql).lab_feedback()
#
# #Auditorium Booking Request
# @app.route('/AuditoriumBookingReq',methods=['GET'])
# #page for booking requests this will show
# #all request for auditorium booking
# def auditorium_booking():
#     return AuditoriumBookingReq(mysql).auditorium_booking()
#
# @app.route('/audi_payment_image',methods=['GET','POST'])
# #payment image for auditorium will sent to admin
# def audi_payment_image():
#     return AuditoriumBookingReq(mysql).audi_payment_image()
#
# @app.route('/auditorium_confirmation',methods=['GET','POST'])
# #admins reply for auditorium booking confirmation
# #reply would be send to customer through email
# def auditorium_feedback():
#     return AuditoriumBookingReq(mysql).auditorium_feedback()
#
# #Field Booking Request
# @app.route('/FieldBookingReq',methods=['GET'])
# #page for booking requests this will show
# #all request for field booking
# def field_booking():
#     return FieldBookingReq(mysql).field_booking()
#
# #payment image will shown to admin
# @app.route('/field_payment_image',methods=['GET','POST'])
# def field_payment_image():
#     return FieldBookingReq(mysql).field_payment_image()
#
# @app.route('/field_confirmation',methods=['GET','POST'])
# #admins reply for field booking confirmation
# #reply would be send to customer through email
# def field_feedback():
#     return FieldBookingReq(mysql).field_feedback()
#
# #Class update method
# @app.route('/ClassUpdate',methods=['GET'])
# #all available classes would be shown
# def class_info():
#     return ClassUpdate(mysql).class_info()
#
# @app.route('/class_delete')
# #admin can delete classroom
# def class_delete():
#     return ClassUpdate(mysql).class_delete()
#
# @app.route('/class_update_data',methods=['GET'])
# #admin can update class info
# def class_update():
#     return ClassUpdate(mysql).class_update()
#
# @app.route('/class_insert_data',methods=['GET'])
# #admin can add new class
# def class_insert():
#     return ClassUpdate(mysql).class_insert()
#
# @app.route('/LabUpdate',methods=['GET'])
# #all available lab will shown
# def lab_info():
#     return LabUpdate(mysql).lab_info()
#
# @app.route('/lab_delete')
# #delete any lab
# def lab_delete():
#     return LabUpdate(mysql).lab_delete()
#
# @app.route('/lab_update_data',methods=['GET'])
# #admin can update lab info
# def lab_update():
#     return LabUpdate(mysql).lab_update()
#
# @app.route('/lab_insert_data',methods=['GET'])
# #admin can add lab
# def lab_insert():
#     return LabUpdate(mysql).lab_insert()
#
#
#
# @app.route('/AuditoriumUpdate',methods=['GET'])
# #all available lab will shown
# def auditorium_info():
#     return AuditoriumUpdate(mysql).auditorium_info()
#
# @app.route('/auditorium_delete')
# #delete any lab
# def auditorium_delete():
#     return AuditoriumUpdate(mysql).auditorium_delete()
#
# @app.route('/auditorium_update_data',methods=['POST'])
# #admin can update lab info
# def auditorium_update():
#     return AuditoriumUpdate(mysql).auditorium_update()
#
# @app.route('/auditorium_insert_data',methods=['POST'])
# #admin can add lab
# def auditorium_insert():
#     return AuditoriumUpdate(mysql).auditorium_insert()
#
#
#
# @app.route('/FieldUpdate',methods=['GET'])
# #all available lab will shown
# def field_info():
#     return FieldUpdate(mysql).field_info()
#
# @app.route('/field_delete')
# #delete any lab
# def field_delete():
#     return FieldUpdate(mysql).field_delete()
#
# @app.route('/field_update_data',methods=['POST'])
# #admin can update lab info
# def field_update():
#     return FieldUpdate(mysql).field_update()
#
# @app.route('/field_insert_data',methods=['POST'])
# #admin can add lab
# def field_insert():
#     return FieldUpdate(mysql).field_insert()
#
# #Munna started adding from here------------------------------------------------->
#
# @app.route('/classRoomBooking', methods=["GET", "POST"])
# def showClassSlotOnSelectedDate():
#     return classBookingClass(mysql).showClassSlot()
#
# @app.route('/classRoomFixedDate', methods=["GET", "POST"])
# def showClassSlotOnFixedDate():
#     return classBookingClass(mysql).showClassSlotOnFixedDate()
#
# @app.route('/selectedSlotRoom', methods=["GET", "POST"])
# def showSelectedSlot():
#     return classBookingClass(mysql).applyforBookig()
#
#
# @app.route('/labBooking', methods=["GET","POST"])
# def showLabStatus():
#     return labBookingClass(mysql).showLabStatus()
#
#
# @app.route('/labFixedDate', methods=["GET", "POST"])
# def showLabSlotOnFixedDate():
#     return labBookingClass(mysql).showLabSlotOnFixedDate()
#
#
# @app.route('/selectedSlotLab', methods=["GET", "POST"])
# def showSelectedLabSlot():
#     return labBookingClass(mysql).applyforLabBookig()
#
#
#
#
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)