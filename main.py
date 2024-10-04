from flask import Flask, request, escape
import os

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    # Vulnerable to XSS
    name = request.args.get('name', '')
    return f"<h1>Hello, {name}!</h1>"
    print("Hello")

if __name__ == '__main__':
    app.run()
