FROM hub.hamdocker.ir/library/python:3.8

WORKDIR /project
ADD . .

RUN pip install pipenv
RUN pipenv install --ignore-pipfile

COPY ./compose/production/django/start /start

ENTRYPOINT ["/start"]
