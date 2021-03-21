#!/usr/local/bin/python

import sys
from pathlib import Path

from dotenv import load_dotenv

code_path = Path("../")
sys.path.append(code_path / "/src")
load_dotenv(dotenv_path=code_path / ".env")


import django

django.setup()

import json

from faker import Faker

faker = Faker()

from users.functions import register_user
from permissions.models import Role, Permission
from permissions.models.permission import ValidPermissions
from permissions.functions import create_permission
from systems.models import System, Genre, Publisher

print("\n\n")

user = register_user(
    email="contact@gamersplane.com", username="Keleth", password="test1234"
)
user.activate()
user.admin = True
user.save()
print("Create first user\n")

guest_role = Role(name="Guest", owner=user)
guest_role.save()
member_role = Role(name="Member", owner=user)
member_role.save()
print("Add Guest and Member roles\n")

user.roles.add(member_role)
user.save()
print("Add Member role to first user\n")

extra_users = []
for i in range(2):
    user = register_user(
        email=faker.email(),
        username=faker.simple_profile()["username"],
        password="test1234",
    )
    user.activate()
    user.roles.add(member_role)
    extra_users.append(user)
print("Created two member users\n")


test_role_1 = Role(name="Test Role 1", owner=extra_users[0])
test_role_1.save()
extra_users[0].roles.add(test_role_1)
test_role_1_admin_permission = create_permission(
    ValidPermissions.ROLE_ADMIN, test_role_1.id
)
test_role_1.permissions.add(test_role_1_admin_permission)


with open("data/systems.json") as f:
    systems_data = json.load(f)

for system_data in systems_data:
    if not system_data.get("basics", False):
        system_data["basics"] = None
    system = System(
        **{k: v for k, v in system_data.items() if k not in ["genres", "publisher"]}
    )
    system.save()
    if system_data["publisher"]:
        publisher, _ = Publisher.objects.get_or_create(
            name=system_data["publisher"]["name"],
            defaults={"website": system_data["publisher"]["site"]},
        )
        system.publisher = publisher
    if system_data["genres"]:
        for genre_data in system_data["genres"]:
            genre, _ = Genre.objects.get_or_create(genre=genre_data)
            system.genres.add(genre)
    print(f"Created system: {system.name}")
print("\n")
