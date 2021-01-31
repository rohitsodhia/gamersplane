from tokens.models.token import Token


class AccountActivation(Token):
    class Meta:
        proxy = True

    model_token_type = Token.TokenTypes.ACCOUNT_ACTIVATION.value
