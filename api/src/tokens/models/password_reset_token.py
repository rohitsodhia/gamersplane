from tokens.models.token import Token, TokenManager


class PasswordResetToken(Token):
    class Meta:
        proxy = True

    model_token_type = Token.TokenTypes.PASSWORD_RESET.value

    objects = TokenManager(token_type=model_token_type)
    all_objects = TokenManager(token_type=model_token_type, available=False)
