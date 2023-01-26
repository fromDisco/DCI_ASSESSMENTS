FROM python:3.8.15-alpine3.16

WORKDIR /app

RUN apk add bash

RUN pip install psycopg2-binary

RUN touch test.txt

COPY . .

ENTRYPOINT python3 helpers.py && python3 -m unittest test.py
CMD tail -f helpers.py
