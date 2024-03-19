from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask Calculator!"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}."

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    result = num1 - num2
    return f"The difference of {num1} and {num2} is {result}."

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f"The product of {num1} and {num2} is {result}."

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    result = num1 / num2
    return f"The division of {num1} by {num2} is {result}."

if __name__ == '__main__':
    app.run(debug=True)
