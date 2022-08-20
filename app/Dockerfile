FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt -y install python3-pip
RUN pip install pipenv

WORKDIR /app

COPY ./Pipfile ./
COPY ./Pipfile.lock ./
RUN pipenv sync

CMD ['pipenv', 'run', 'uvicorn', 'app.asgi:application', '--reload']

