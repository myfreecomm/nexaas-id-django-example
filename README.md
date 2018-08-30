# Nexaas ID Django example

Example code for connecting to Nexaas ID using Django.

## Installation

```sh
git clone https://github.com/myfreecomm/nexaas-id-django-example.git
cd nexaas-id-django-example/
python3 -mvenv .env
source .env/bin/activate
pip install -U pip
./setup.py develop
cp .env.test .env.development
echo 'DEBUG=1' >> .env.development
./manage.py migrate
```

You must edit `.env.development` in order to provide Nexaas ID client
application credentials.

### Configuring Test Application on Nexaas ID development area

In [Nexaas ID development area](http://localhost:3000/applications), create and
configure your application like the following example:

- Sign out URL for Widget: `http://localhost:8000/oauth/signout/`
- Callback URI: `http://localhost:8000/oauth/callback/`

<div align="center">
  <img alt="Example"
       src="https://github.com/myfreecomm/nexaas-id-django-example/raw/master/nexaas_id_django_example/static/example.jpg" />
</div>

Links for development area:

- [Localhost](http://localhost:3000/applications)
- [Sandbox](https://sandbox.id.nexaas.com/applications)
- [Production](https://id.nexaas.com/applications)

## Running server

```sh
cd nexaas-id-django-example/
source .env/bin/activate
./manage.py runserver
```

Use:

```sh
sensible-browser http://localhost:8000/
```
