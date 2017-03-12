FROM python:3.5

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements/test.txt

COPY ./features /testing/features

WORKDIR /testing

CMD ["behave"]
