###########
# BUILDER #
###########

# pull official base image
FROM python:3.9-alpine as builder

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    openssl libffi-dev openssl-dev

# install openssl dependencies
RUN apk add openssl libffi-dev openssl-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

# lint
RUN pip install --upgrade pip
RUN pip install flake8

COPY ./web /usr/src/web/

RUN flake8 --ignore=E501,F401,F403 .

# install dependencies
COPY ./docker/prod/web/requirements.txt  ./requirements.txt

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/web/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9-alpine

# create directory for the app user
RUN mkdir -p /home/www

# create the app user
RUN addgroup -S www && adduser -S www -G www

# create the appropriate directories
ENV HOME=/home/www
ENV APP_HOME=/home/www/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev
# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

COPY --from=builder /usr/src/web/wheels /wheels
COPY --from=builder /usr/src/web/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./docker/prod/web/entrypoint.sh /entrypoint.sh
COPY ./docker/prod/worker/entrypoint.sh  /entrypoint.worker.sh

# copy project
COPY . $APP_HOME

# chown all the files to the www user
RUN chown -R www:www $APP_HOME

RUN chown -R www:www /entrypoint.sh
#RUN chmod -cR u+rwX $APP_HOME

RUN chmod +x /entrypoint.sh

## change to the www user
USER www

## run entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
