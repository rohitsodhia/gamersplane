from auth.models.user import User


class TestUser:
    def test_valid_pass():
        assert User.validate_pass("abcdefgh")
