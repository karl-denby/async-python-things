FROM alpine:3.8

RUN apk add python3 && \
    apk add alpine-sdk && \
    python3 -m pip install pipenv

COPY . ./
RUN pipenv install

CMD pipenv run app.py
