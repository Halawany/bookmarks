FROM python:3.11-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookmarks

COPY Pipfile Pipfile.lock /bookmarks/
RUN pip install pipenv && pipenv install --system 

COPY . /bookmarks/