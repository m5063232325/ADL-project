FROM python:3.8

COPY ./volume /app

WORKDIR /app

RUN pip install -r requirements.txt
CMD python hello.py

