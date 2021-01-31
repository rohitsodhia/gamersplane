from auth.models import User
from tokens.models import AccountActivation


def register_user(new_user: User) -> None:
    new_user.save()
    account_activation_token = AccountActivation(user=new_user)
    account_activation_token.save()
    new_user.send_activation_email()
