# Flask-Sendwithus

[![Circle CI](https://circleci.com/gh/jmagnusson/flask-sendwithus.svg?style=shield&circle-token=56ac6919ffb79a741dcfab873f26d281c17ae23d)](https://circleci.com/gh/jmagnusson/flask-sendwithus/tree/master)
[![PyPI version](https://img.shields.io/pypi/v/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![Downloads from PyPI per month](https://img.shields.io/pypi/dm/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![License](https://img.shields.io/pypi/l/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![Available as wheel](https://img.shields.io/pypi/wheel/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![PyPI status (alpha/beta/stable)](https://img.shields.io/pypi/status/Flask-Sendwithus.svg)](https://pypi.python.org/pypi/Flask-Sendwithus/)
[![codecov.io](http://codecov.io/github/jmagnusson/flask-sendwithus/coverage.svg?branch=master)](http://codecov.io/github/jmagnusson/flask-sendwithus?branch=master)


## About

Forwards-compatible Flask extension to interact with the [sendwithus](https://www.sendwithus.com/) API.

## Installation

    pip install Flask-Sendwithus

## Documentation

Uses the standard extension pattern. Example:

```python
>>> from flask import Flask
>>> from flask_sendwithus import Sendwithus

>>> app = Flask(__name__)
>>> app.config['SENDWITHUS_API_KEY'] = 'YOUR-API-KEY'
>>> sendwithus = Sendwithus()
>>> sendwithus.init_app(app)
>>> r = sendwithus.send(
    email_id='YOUR-EMAIL-ID',
    recipient={'address': 'us@sendwithus.com'})
>>> print(r.status_code)
200
```

See [the official python client's documentation](https://github.com/sendwithus/sendwithus_python) for further info on what methods are available. All methods found on the `sendwithus.api` instance is proxied on the Flask-Sendwithus's instance.
