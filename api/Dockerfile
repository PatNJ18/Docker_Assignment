FROM python:3.7-alpine
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000



COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app.py /app

CMD ["flask", "run"]
