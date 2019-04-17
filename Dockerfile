FROM alpine:3.8

RUN apk add python3 && \
    apk add python3-dev && \
    apk add alpine-sdk && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install pipenv && \
    python3 -m pip install chatterbot

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pipenv install
COPY . /app

EXPOSE 5000
CMD ["pipenv", "run", "python", "app.py"]