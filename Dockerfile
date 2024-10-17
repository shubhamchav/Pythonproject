FROM python:3.8-slim-buster
LABEL maintainer="onkarko"

WORKDIR /python-docker
COPY . /python-docker

RUN pip3 install -r requirements.txt

ENV FLASK_APP=/python-docker/run.py
ENV FLASK_ENV=development
ENV APPLICATION_ENV=dev
ENV FLASK_DEBUG=1

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5002" ]
