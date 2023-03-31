from flask import Flask,request,render_template
from re import *
import re
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("form1.html")
@app.route('/ajax',methods=['POST'])
def calc():
    if request.method == 'POST':
        text = request.form["qwerty"]
        c = findall('\D+',text)
        b = findall('\d+',text)
        print(c)
        print(b)
        print(c)
        if c[0] == "+":
            s = int(b[0]) + int(b[1])
            print(f"{b[0]} + {b[1]} = {s}")
            return f"{b[0]} + {b[1]} = {s}"
        if c[0] == "-":
            s = int(b[0]) - int(b[1])
            print(f"{b[0]} - {b[1]} = {s}")
            return f"{b[0]} - {b[1]} = {s}"
        if c[0] == "*":
            s = int(b[0]) * int(b[1])
            print(f"{b[0]} * {b[1]} = {s}")
            return f"{b[0]} * {b[1]} = {s}"
        if c[0] == "/":
            s = int(b[0]) / int(b[1])
            print(f"{b[0]} / {b[1]} = {s}")
            return f"{b[0]} / {b[1]} = {s}"
    return "Error"
if __name__ == '__main__':
    app.run(port=8081,host='127.0.0.1')

