import requests
import json
from line_notify.secret import line
# POST https://notify-bot.line.me/oauth/token


def fetch_token(code):
    headers = { 'Content-type': 'application/x-www-form-urlencoded' }
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': line['uri'],
        'client_id': line['client_id'],
        'client_secret': line['client_secret']
    }

    res = requests.post('https://notify-bot.line.me/oauth/token', 
                        headers=headers, data=payload)
    res_json = json.loads(res.text)

    token = res_json['access_token']

    # log: Users' Access_token
    print('Access_token: ' + token)
    save_token(token)


    return token

def save_token(new_token):
    file_name = 'tokens.json'
    check_file_exist(file_name)

    with open('tokens.json', 'r', encoding='utf-8') as file:
        tokens = json.load(file)
        
    tokens.append(new_token)
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(tokens, file)
        
        
def check_file_exist(file_name):
    try:
        file = open(file_name, 'r')
    except IOError:
        with open(file_name, 'w') as f:
            f.write('[]')

def check_token_exist(new_token):
    with open('tokens.json', 'r', encoding='utf-8') as file:
        tokens = json.load(file)
        if new_token in tokens:
            return True
        else:
            return False

