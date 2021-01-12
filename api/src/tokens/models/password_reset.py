from tokens.models.token import TokenManager, Token


class PasswordResetManager(TokenManager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(token_type=Token.TokenTypes.PASSWORD_RESET)


class PasswordReset(Token):
    class Meta:
        proxy = True

    objects = PasswordResetManager()
