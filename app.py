import re
from firebase import add_new_usermail
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

def validate_email(to_validate):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(pattern, to_validate):
        return True
    return False

@app.route('/register_email', methods = ['POST'])
def register_email():
    user_email = request.form['mail-id']
    if validate_email(user_email):
        add_new_usermail(user_email)
        return "<center> <h1> Successfully Registered </h1> </center>"
    return "<center> <h1> Wrong Email</h1> </center>"

if __name__ == '__main__':
    app.run(debug = True)