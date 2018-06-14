import requests
# POST https://notify-api.line.me/api/notify


def send_success_msg(token):
    headers = {'Authorization': 'Bearer ' + token}
    payloads = {'message': 'Hello I\'m Capoo'}
    res = requests.post('https://notify-api.line.me/api/notify', 
                    headers=headers, params=payloads)

    if(res.status_code == requests.codes.ok):
        print('success: status ' + str(res.status_code))
    else:
        print('fail: status ' + str(res.status_code))



if __name__ == "__main__":
    send_success_msg()
