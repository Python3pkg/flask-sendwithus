import pytest
from flask import Flask
from flask_sendwithus import Sendwithus

TEST_API_KEY = '1234567890'
TEST_TEMPLATE_ID = 'tem_vfTEaSKlXbtUci4so8zA3e'
TEST_TEMPLATE_EMAIL = 'm@jacobian.se'


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SENDWITHUS_API_KEY'] = TEST_API_KEY
    return app


@pytest.fixture
def sendwithus(app):
    sendwithus = Sendwithus()
    sendwithus.init_app(app)
    return sendwithus


def test_app_factory_pattern(app):
    sendwithus = Sendwithus()
    sendwithus.init_app(app)
    with pytest.raises(RuntimeError):
        assert sendwithus.api_key == TEST_API_KEY
    with app.test_request_context():
        assert sendwithus.api_key == TEST_API_KEY


def test_attribute_access(app, sendwithus):
    with pytest.raises(RuntimeError):
        assert sendwithus.api_key == TEST_API_KEY
    with app.test_request_context():
        with pytest.raises(AttributeError):
            sendwithus.nonexisting_attribute_123
    with app.test_request_context():
        assert sendwithus.api
        assert sendwithus.render == sendwithus.api.render


def test_bad_auth_api_calls(app, sendwithus):
    with app.test_request_context():
        resp = sendwithus.send(TEST_TEMPLATE_ID, TEST_TEMPLATE_EMAIL)
        assert resp.status_code == 403

        resp = sendwithus.render(TEST_TEMPLATE_ID, {})
        assert resp.status_code == 403
