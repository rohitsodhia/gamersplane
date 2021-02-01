from tokens.models.token import Token


class PasswordResetToken(Token):
    class Meta:
        proxy = True

    model_token_type = Token.TokenTypes.PASSWORD_RESET.value
