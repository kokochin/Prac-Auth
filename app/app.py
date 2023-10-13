from flask import Flask, redirect, url_for, render_template, request, jsonify,abort,Response
import json
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

'''-----------------認証用の記述-----------------'''

auth = HTTPBasicAuth()

users = {
    "kokoro": "yamasaki",
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

'''-----------------以下はテストページの記述(後で消す)-----------------'''

# webサーバが立ち上がっているか確認するようのルーティング
@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():    
    return ('<h1>認証成功</h1>')

if __name__ == "__main__":
    app.run(debug=True)
