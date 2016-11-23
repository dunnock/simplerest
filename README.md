# simplerest
Python Django simplest server for debugging REST APIs with authentication

# requires

* python3
* django

# usage

Supports basic user REST, enough to serve as a mock for your client. It will output all the requests to the console. Also provides CORS headers allowing communication with the server from a different url.

After starting server you can see description of the REST API following the link [localhost](http://localhost:8000/), admin interface is avaialble via [localhost admin](http://localhost:8000/admin/)

# setup

1. create virtualenv

  virtualenv env
  source env/bin/activate

2. install dependencies

    pip install django
    pip install djangorestframework

3. create database and user

    python manage.py migrate
    python manage.py createsuperuser

4. start server

    python manage.py runserver

