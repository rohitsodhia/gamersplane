from tokens.models.token import TokenManager, Token


class AccountActivationManager(TokenManager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(token_type=Token.TokenTypes.ACCOUNT_ACTIVATION)


class AccountActivation(Token):
    class Meta:
        proxy = True

    objects = AccountActivationManager()
