import math
from flask import Flask,request,render_template
from re import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("form1.html")
@app.route('/ajax',methods=['POST'])
def calc():
    if request.method == 'POST':
        text = request.form["qwerty"]
        c = findall('[\\+,\\-,*,/,%,V]',text)
        b = text.split(c[0])
        print(c)
        print(b)
        if c[0] == "+":
            s = float(b[0]) + float(b[1])
            print(f"{b[0]} + {b[1]} = {s}")
            return f"{b[0]} + {b[1]} = {s}"
        if c[0] == "-":
            s = float(b[0]) - float(b[1])
            print(f"{b[0]} - {b[1]} = {s}")
            return f"{b[0]} - {b[1]} = {s}"
        if c[0] == "*":
            s = float(b[0]) * float(b[1])
            print(f"{b[0]} * {b[1]} = {s}")
            return f"{b[0]} * {b[1]} = {s}"
        if c[0] == "/":
            try:
                s = float(b[0]) / float(b[1])
                print(f"{b[0]} / {b[1]} = {s}")
                return f"{b[0]} / {b[1]} = {s}"
            except ZeroDivisionError:
                return "на 0 нельзя делить"
        if c[0] == "%":
            s = float(b[0]) / 100
            print(f"{b[0]} %  = {s}")
            return f"{b[0]} % = {s}"
        if c[0] == "V":
            s = math.sqrt(float(b[0]))
            print(f"{b[0]} sqrt  = {s}")
            return f"{b[0]} sqrt = {s}"
    return "Error"
if __name__ == '__main__':
    app.run(port=8081,host='127.0.0.1')

