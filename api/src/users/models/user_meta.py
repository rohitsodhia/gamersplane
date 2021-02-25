from django.core.exceptions import ValidationError
from django.db import models


class UserMeta(models.Model):
    class Meta:
        db_table = "user_meta"

    class MetaKeys(models.TextChoices):
        AVATAR_EXT = "avatarExt", "Avatar Extension"
        LOCATION = "location", "Location"
        NEW_GAME_MAIL = "newGameMail", "New Game Mail"
        POST_SIDE = "postSide", "Post Side"
        REFERENCE = "reference", "Reference"
        SHOW_AVATARS = "showAvatars", "Show Avatars"
        SHOW_TZ = "showTZ", "Show Timezone"
        TIMEZONE = "timezone", "Timezone"

    user = models.ForeignKey(
        "users.User", db_column="userId", related_name="meta", on_delete=models.PROTECT
    )
    key = models.CharField(max_length=32, choices=MetaKeys.choices)
    value = models.CharField(max_length=200)

    def full_clean(self, exclude=None, validate_unique=True):
        if self.key == self.MetaKeys.POST_SIDE:
            if self.value.lower() not in ["l", "r"]:
                raise ValidationError("Post Side must either be 'l' or 'r'")
            self.value = self.value.lower()
        elif (
            self.key
            in [
                self.MetaKeys.NEW_GAME_MAIL,
                self.MetaKeys.SHOW_AVATARS,
                self.MetaKeys.SHOW_TZ,
            ]
            and type(self.value) is not bool
        ):
            raise ValidationError(f"{self.key} must be a boolean")
        super().full_clean(exclude, validate_unique)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
