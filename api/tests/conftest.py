import pytest
from django.core.management import call_command

from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client, app.test_request_context():
            yield client
