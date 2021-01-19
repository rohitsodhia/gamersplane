from tokens.models import Token


class TestToken:
    def test_generate_token(self):
        token = Token()
        assert token.token == ""
        token.generate_token()
        assert token.token != "" and len(token.token) == 16
        current_token = token.token
        token.generate_token()
        assert token.token == current_token
