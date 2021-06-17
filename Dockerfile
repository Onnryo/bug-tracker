FROM python:3.9.5-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev python3-dev 
RUN apk add --update --no-cache jpeg-dev zlib-dev
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

# Copy project
COPY ./src /app

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

#USER user
