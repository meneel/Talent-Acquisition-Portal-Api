# ==========================================
#   Copyright (c) 2020 Debmalya Pramanik   #
# ==========================================

# -------------------------------------------------------------------
#   Mnemonic:   Dockerfile
#   Abstract:   Hello-World Flask REST-API Docker Template
#
#   Date:       15 April 2021
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM tiangolo/uwsgi-nginx-flask:python3.8
# MAINTAINER Debmalya Pramanik <dPramanik.official@gmail.com>

ENV INSTALL_PATH /usr/src/helloworld
RUN mkdir -p $INSTALL_PATH

# install net-tools
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR $INSTALL_PATH

# setting up environment variables
# application specific ENVIRONMENT VARIABLES
# can be either set from this Dockerfile
# or individual file can be configured under
# `.env` and `./app/main/.env` directory.
# getting started, specific environment variables
# are defined in Dockerfile for understanding as
# mentioned below:
#
# ENVIRONMENT VARIABLES for `.env`
#
# ENV port
# ENV host
# ENV PROJECT_ENV_NAME
#
# ENVIRONMENT VARIABLES for `./app/main/.env`
#
# ENV database_host
# ENV database_port
# ENV username
# ENV password
# ENV DATABASE_URL
# ENV dev_db
#
# NOTE - dummy `.env` files are present with
# an extension `.env.bkp`


# setup flask environment
# install all requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy all files and folder to docker
COPY . .

# run the application in docker environment
CMD [ "python", "./manage.py" ] # this will run forever
