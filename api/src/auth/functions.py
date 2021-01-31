from auth.models import User
from tokens.models import AccountActivation


def register_user(new_user):
    # new_user.save()
    account_activation_token = AccountActivation(user=new_user)
    breakpoint()
    # new_user.send_activation_email()
