FROM python:3.8-alpine

WORKDIR /app/

RUN apk update && apk add --no-cach --virtual bash git gcc g++

RUN python -m pip install --upgrade pip

COPY . /app/

CMD ["python", "game.py"]