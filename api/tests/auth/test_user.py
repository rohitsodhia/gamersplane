from users.models import User


class TestUser:
    VALID_PASS = "abcdefgh"

    def test_validate_password(self):
        assert User.validate_password(self.VALID_PASS) == []

    def test_validate_short_pass(self):
        assert User.validate_password("abcd") == ["pass_too_short"]

    def test_hash_pass(self):
        assert type(User.hash_pass(self.VALID_PASS)) == str

    def test_set_password(self):
        user = User()
        assert user.password == ""
        user.set_password(self.VALID_PASS)
        assert user.password != ""
        assert type(user.password) == str

    def test_set_bad_password(self):
        user = User()
        assert user.password == ""
        valid = user.set_password("asdf")
        assert not valid

    def test_check_password(self):
        user = User()
        user.set_password(self.VALID_PASS)
        assert user.check_pass(self.VALID_PASS)
