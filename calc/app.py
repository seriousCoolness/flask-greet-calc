# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_page():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return f"{add(a,b)}"

@app.route("/sub")
def sub_page():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return f"{sub(a,b)}"

@app.route("/mult")
def mult_page():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return f"{mult(a,b)}"

@app.route("/div")
def div_page():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return f"{div(a,b)}"

@app.route("/math/<operation>")
def math_page(operation):
    #haha funy callback system usiong a dictionary
    op_dict = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return f"{op_dict[operation](a,b)}"

