# pull official base image
FROM python:3.9-alpine

ENV HOME /usr/src/web
# set work directory
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY  '22+sg%5+##a=^-$o58(1q9(^r@cjl-p0r3m^x9@-#i=1qcs2y2'
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./docker/dev/web/requirements.txt  ./requirements.txt
RUN pip install -r requirements.txt

RUN flake8 --ignore=E501,F401,F403 .

# copy entrypoint.sh
COPY ./docker/dev/web/entrypoint.sh /entrypoint.sh
# copy project
COPY ./web /usr/src/web/

# run entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]

