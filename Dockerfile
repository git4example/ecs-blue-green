FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV APP_PORT 5000

ENTRYPOINT ./app.py
