from mock import patch

from auth.models import User


class TestUser:
    def test_valid_pass(self):
        assert User.validate_pass("abcdefgh")
