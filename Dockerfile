from python:2.7-alpine

add app.py /app/

RUN pip install requests flask


CMD python /app/app.py
