from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'