FROM python:3.8-slim-buster

WORKDIR /app/config/

COPY requirements.txt requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
