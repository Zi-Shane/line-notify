from flask import Flask, request, render_template
from line_notify.fetchToken import fetch_token
from line_notify.sendSuccess import send_success_msg


app = Flask(__name__)

@app.route("/")
def home():
    code = request.args.get('code')
    if code is None:
        # log: first time get this page
        print('no code parameter')

        return render_template('home.html')
    else:
        # log: Users' Authentication code
        print('Authentication code: ' + code)
        token = fetch_token(code)
        send_success_msg(token)
        return render_template('success.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')