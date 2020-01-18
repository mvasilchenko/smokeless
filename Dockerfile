FROM python:3.7.2

RUN apk update \
    && apk add gcc python3-dev musl-dev build-base postgresql-dev

WORKDIR /app

RUN pip install --upgrade pip

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN pipenv install --system -d

COPY . /app
