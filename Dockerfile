# pull official base image
FROM python:3.9-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# set working directory
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && pip install -r requirements.txt
    
COPY . /code/

EXPOSE 80

CMD ["sh", "deploy_fandogh.sh"]