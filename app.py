from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello, World!'

def login(username, password):
    if username == 'admin' and password == 'password':
        return True
    return False


@app.route('/login', methods=['POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')

    if login(username, password):
        return 'Login successful'
    else:
        return 'Login failed'


if __name__ == '__main__':
    app.run()
