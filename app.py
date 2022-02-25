from operator import index
import re
from flask import Flask,render_template,request
from password_generator import *
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def display():
    return render_template("index.html")
@app.route('/password',methods=["GET","POST"])
def password_generator():
    password_length=int(request.form['pass_len'])
    password=generate_password(length=password_length)
    if password=="valid_password_not_generated":
        return render_template("error.html")
    else:
        return  render_template("password_display.html",password=password)
if __name__ == '__main__':
    app.run(debug=True,port=8000)