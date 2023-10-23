FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookmarks

COPY Pipfile Pipfile.lock /bookmarks/
RUN pip install pipenv && pipenv install --system 

COPY . /bookmarks/