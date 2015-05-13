from flask import Flask, render_template, redirect, request
from wtforms import TextField, PasswordField
from flask.ext.wtf import Form
from utils import load_keys
from tasks import getTweetsByWords, test_task, error_handler
import argparse

keys_path = None
#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(__name__)

app.debug=True
app.secret_key='qleg917zqaexjccwitkwlitu5bb11n9z4jkv7b14r2bc1o8ns8pmmfwtyy2lm6l3'

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('uassword')
    apikey = TextField('apikey')

@app.route('/', methods=('GET','POST'))
def index():
    data = load_keys(keys_path)
    messages = getTweetsByWords.apply_async(args=[data, ""], link_error=error_handler.s())
    #test_task.apply_async().get()
    return render_template('index.html', messages=messages)


@app.route('/login', methods=('GET','POST'))
def login():
    loginform = LoginForm()
    if request.method == 'POST':
        return redirect('/')
    return render_template('login.html', form=loginform)

if __name__ == '__main__':
    parsing = argparse.ArgumentParser()
    parsing.add_argument('--keys', help='load files with keys for connect to Twitter')
    keys_path = parsing.parse_args().keys
    app.run()
