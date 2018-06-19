from flask import Flask, request, render_template, jsonify
from line_notify.secret import line
from line_notify.fetchToken import fetch_token
from line_notify.sendSuccess import send_success_msg
import json


app = Flask(__name__)

@app.route("/")
def home():
    code = request.args.get('code')
    if code is None:
        # log: first time get this page
        print('no code parameter')

        return render_template('home.html', 
                                uri=line['uri'], 
                                client_id=line['client_id'])
    else:
        # log: Users' Authentication code
        print('Authentication code: ' + code)
        token = fetch_token(code)
        send_success_msg(token)

        return render_template('success.html')

@app.route("/json")
def token_api():
    with open('tokens.json', 'r', encoding='utf-8') as file:
        tokens = json.load(file)

    return jsonify(tokens)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30000)