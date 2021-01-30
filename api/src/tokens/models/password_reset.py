from tokens.models.token import Token


class PasswordReset(Token):
    class Meta:
        proxy = True
        token_type = Token.TokenTypes.PASSWORD_RESET
