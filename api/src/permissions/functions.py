from permissions.models import Permission
from permissions.models.permission import ValidPermissions


def create_permission(permission: ValidPermissions, *args) -> Permission:
    permission_obj = Permission()
    permission_obj.set_permission(permission, *args)
    permission_obj.save()
    return permission_obj
