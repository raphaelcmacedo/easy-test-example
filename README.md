# Tasks
An example of easy text https://github.com:raphaelcmacedo/easy-test

[![Build Status](https://travis-ci.org/raphaelcmacedo/easy-test-example.svg?branch=master)](https://travis-ci.org/raphaelcmacedo/easy-test-example)
[![Code Health](https://landscape.io/github/raphaelcmacedo/easy-test-example/master/landscape.svg?style=flat)](https://landscape.io/github/raphaelcmacedo/easy-test-example/master)

## How to develop?

1. Clone the repository.
2. Create a virtualenv with Python 3.5
3. Activate virtualenv.
4. Install dependencies.
5. Configure the instance with the .env
6. Run the tests.

```console
git clone git@github.com:raphaelcmacedo/easy-test-example.git easy_test_example
cd easy_test_example
python -m venv .ete
source .ete/bin/activate
pip install -r requirements-dev.txt
cp easy_test_example/contrib/env-sample .env
python manage.py test
```

## How to deploy?

1. Create an instance in heroku.
2. Send the settings to the heroku.
3. Define a safe SECRET_KEY for instance.
4. Set DEBUG = False
5. Send the code to the heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```

