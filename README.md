# Code Coverage

<!-- [![codecov](https://codecov.io/gh/med1213/python-unittest/branch/master/graph/badge.svg)](https://codecov.io/gh/med1213/python-unittest) -->

[![codecov](https://codecov.io/gh/med1213/python-unittest/branch/master/graph/badge.svg)](https://app.codecov.io/gh/med1213/python-unittest/branch/master)

# SBS-Lucky_Draw-Web-API

This application enables Django powered websites to have multiple tenants via PostgreSQL schemas. A vital feature for every Software-as-a-Service website.

    # Creat a new database
    CREATE DATABASE 'lucky_draw'

## Basic Settings for Development

Activate environment

    python3 -m venv venv
    source venv/bin/activate

## Install dependencies

    pip install -r dev-requirements.txt

## Install redis on ubuntu 22.04

    sudo apt update
    sudo apt install redis-server

## Testing Redis

    sudo systemctl status redis

## Configuring Redis

    sudo nano /etc/redis/redis.conf
    Inside the file, find the supervised directive. The supervised directive is set to => no by default, change this to => systemd
    sudo systemctl restart redis.service
    sudo systemctl status redis

## Binding to localhost

    sudo nano /etc/redis/redis.conf
    Locate this line and make sure it is uncommented (remove the # if it exists):
    . . .
    bind 127.0.0.1 ::1
    . . .
    sudo systemctl restart redis

## Configuring a Redis Password

    sudo nano /etc/redis/redis.conf
    . . .
    requirepass your_password
    . . .
    sudo systemctl restart redis.service

To test that the password works, open up the Redis client:
redis-cli
auth your_redis_password

To view your redis password:
redis-cli
config get requirepass

Basic Settings
You’ll have to make the following creations to your your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'
    JWT_SECRET_KEY='your_jwt_secret_key'
    Redis_host=redis://:your_password@localhost:6379

## Make migrations and Apply to database # create migrations files (every new django app)

    python manage.py makemigrations
    python manage.py makemigrations period bill prize candidate province district about slide footer village post prize_type period_type winner user_profile live_data lucky_draw
    python manage.py migrate

## Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser
    python manage.py runserver

## Go to

    localhost:8000/admin/ or localhost:8000/swagger/

## For testing

    python3 manage.py test
    coverage run manage.py test -v 2 && coverage report
    coverage run manage.py test -v 2 && coverage report && coverage html

If show this error "Type 'yes' if you would like to try deleting the test database 'test_lucky_draw', or 'no' to cancel:"
delete file "**init**.py" then create a new one

## Create a new model

    cd apps
    python ../manage.py startapp "folder name"

"# python-unittest"
