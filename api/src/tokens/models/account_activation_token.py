from tokens.models.token import Token


class AccountActivationToken(Token):
    class Meta:
        proxy = True

    model_token_type = Token.TokenTypes.ACCOUNT_ACTIVATION.value
