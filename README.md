# line-notify
## Pre-job
1.  Add your own line-notify service  
https://notify-bot.line.me/zh_TW/
2. Clone this repository
3. Change your own client_id, secret and url by secret_template.py
    1. run command: 
        ```bash
        cp secret_temple.py secret.py
        ```
    2. change your own client_id, client_secret and uri in secret.py
---
## Usage
- python
    1.  Install dependencies
        ```bash
        pip install -r ./flask/requirements.txt
        ```
    2.  Execute application
        ```bash
        python run.py
        ```
- docker
    1. run by docker
        ```bash
        docker-compose up -d
        ```