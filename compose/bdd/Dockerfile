FROM python:3-onbuild

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements/test.txt

WORKDIR /testing
