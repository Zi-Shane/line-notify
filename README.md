# line-notify
## Pre-job
1.  Add your own line-notify service  
https://notify-bot.line.me/zh_TW/
2. Clone this repository
## Usage
1.  Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
2.  Change your own client_id, secret and url by secret_template.py
    1. run command: 
    ```bash
    cp secret_temple.py secret.py
    ```
    2. change your own client_id, client_secret and uri in secret.py
3.  Execute application
    ```bash
    python run.py
    ```
