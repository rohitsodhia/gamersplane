import random
import string

from django.db import models

from auth.models import User

from helpers.email import get_template, send_email


class PasswordReset(models.Model):
    class Meta:
        db_table = "password_resets"
        indexes = [models.Index(fields=["key"])]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    requestedOn = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=16)
    used = models.BooleanField(default=False)

    def generate_key(self):
        if self.key:
            pass
        lettersAndDigits = string.ascii_letters + string.digits
        self.key = "".join(random.choices(lettersAndDigits, k=16))

    def email(self):
        email_content = get_template(
            "auth/templates/reset_password.html",
            reset_link="http://gamersplane.com/login/resetPass/" + self.key,
        )
        send_email(self.email, "Password reset for Gamers' Plane", email_content)

    @staticmethod
    def valid_key(key, email=None, get_obj=False):
        password_reset = PasswordReset.objects.filter(key=key, used=False)
        if email:
            user = User.objects.get(email=email)
            password_reset = password_reset.filter(user=user)

        if get_obj:
            return password_reset[0]
        return True if password_reset else False
