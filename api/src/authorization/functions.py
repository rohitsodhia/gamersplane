from envs import SERVER_NAME
from helpers.email import get_template, send_email
from users.models import User
from tokens.models import AccountActivationToken


def get_activation_link(user: User) -> str:
    try:
        account_activation_token = AccountActivationToken.objects.get(user=user)
    except AccountActivationToken.DoesNotExist:
        account_activation_token = AccountActivationToken(user=user)
        account_activation_token.save()

    if not user.username:
        raise ValueError

    return f"{SERVER_NAME}/activate/{account_activation_token.token}"


def send_activation_email(user: User) -> None:
    email_content = get_template(
        "authorization/templates/activation.html",
        activation_link=get_activation_link(user),
    )
    send_email(user.email, "Activate your Gamers' Plane account!", email_content)
