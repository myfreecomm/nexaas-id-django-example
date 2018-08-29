# Nexaas ID Django example

Example code for connecting to Nexaas ID using Django.

## Installation

```sh
git clone https://github.com/myfreecomm/nexaas-id-django-example.git
cd nexaas-id-django-example/
python -mvenv .env
source .env/bin/activate
./setup.py develop
./manage.py migrate
```

## Running server

```sh
cd nexaas-id-django-example/
source .env/bin/activate
./manage.py runserver
```

Use:

```sh
sensible-browser http://127.0.0.1:8000/
```