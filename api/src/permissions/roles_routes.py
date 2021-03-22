from flask import Blueprint, request, g
from django.db import models

from helpers.decorators import logged_in
from helpers.response import response
from helpers.endpoint import require_values

from users.models import User
from permissions.models import Role, Permission
from permissions.models.permission import ValidPermissions

roles = Blueprint("roles", __name__, url_prefix="/roles")


@roles.route("/", methods=["GET"])
@logged_in
def list_roles():
    args = request.args
    roles = Role.objects
    if args.get("filter"):
        roles = roles.filter(name__icontains=args.get("filter"))
    if not args.get("all") and not g.user.admin:
        roles = roles.filter(users__id=g.user.id)
    if not issubclass(type(roles), models.QuerySet):
        roles = roles.all()
    roles_list = []
    for role in roles:
        roles_list.append(
            {
                "id": role.id,
                "name": role.name,
                "owner": {
                    "id": role.owner.id,
                    "username": role.owner.username,
                },
                "member": bool(role.users.filter(id=g.user.id)),
                "admin": g.user.admin,
            }
        )
    role_admins = [
        int(permission.permission.split("_")[2])
        for permission in Permission.objects.filter(
            permission__startswith="role_admin_"
        )
    ]
    for role in roles_list:
        if role["id"] in role_admins:
            role["admin"] = True

    return response.success({"roles": roles_list})


@roles.route("/<user_id>", methods=["GET"])
@logged_in(permissions="manage_users")
def list_user_roles(user_id):
    user = User.objects.get(id=user_id)
    roles_list = []
    for role in user.roles.all():
        roles_list.append(
            {
                "id": role.id,
                "name": role.name,
                "owner": {
                    "id": role.owner.id,
                    "username": role.owner.username,
                },
                "member": bool(role.users.filter(id=g.user.id)),
                "admin": g.user.admin,
            }
        )
    role_admins = []
    for permission in user.permissions:
        if permission.startswith(ValidPermissions.ROLE_ADMIN.value[0]):
            role_admins.append(int(permission.split("_")[2]))
    for role in roles_list:
        if role["id"] in role_admins:
            role["admin"] = True

    return response.success({"roles": roles_list})
