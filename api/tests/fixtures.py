import pytest

from faker import Faker


@pytest.fixture
def faker():
    return Faker()
