FROM mysql:8
ENV MYSQL_ROOT_PASSWORD 100senha
COPY ./data.sql /docker-entrypoint-initdb.d/data.sql

FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
