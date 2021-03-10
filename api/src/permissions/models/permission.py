from enum import Enum

from django.db import models


class ValidPermissions(Enum):
    ROLE_ADMIN = "role_admin_", "<role_id>"


class Permission(models.Model):
    class Meta:
        db_table = "permissions"

    permission = models.CharField(max_length=64, unique=True)

    def __init__(self, *args, **kwargs) -> None:
        self._valid_permission = False
        super().__init__(*args, **kwargs)

    def set_permission(self, permission: ValidPermissions, *args):
        if type(permission) is not ValidPermissions:
            raise ValueError(f"'{permission}' is not a ValidPermission")
        if type(permission.value) == tuple:
            self._valid_permission = True
            permission_val = ""
            arg_key = 0
            for v in permission.value:
                if v[0] == "<":
                    try:
                        permission_val += str(args[arg_key])
                    except IndexError:
                        raise ValueError(
                            f"Not enough arguments passed for '{permission.value}'"
                        )
                    arg_key += 1
                else:
                    permission_val += v
            self.permission = permission_val
        else:
            self.permission = permission.value

    def save(self, **kwargs) -> None:
        if not self._valid_permission:
            raise ValueError(f"Permission not set through set_permission")
        return super().save(**kwargs)
