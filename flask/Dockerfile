FROM python:3.6.5

# COPY ./requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app

# RUN apk update && apk add \
#         libuuid \
#         pcre \
#         mailcap \
#         gcc \
#         libc-dev \
#         linux-headers \
#         pcre-dev \
#     && pip install -r requirements.txt \
#     && apk del \
#         gcc \
#         libc-dev \
#         linux-headers 
RUN pip install -r requirements.txt

EXPOSE 30000

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
# ENTRYPOINT [ "python3" ]
# CMD [ "run.py" ]


