FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc build-base libffi-dev mariadb-dev python-dev py-bcrypt

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
