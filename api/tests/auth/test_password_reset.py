from auth.models import PasswordReset


class TestPasswordReset:
    def test_generate_key(self):
        password_reset = PasswordReset()
        assert password_reset.key == ""
        password_reset.generate_key()
        assert password_reset.key != "" and len(password_reset.key) == 16
        current_key = password_reset.key
        password_reset.generate_key()
        assert password_reset.key == current_key
