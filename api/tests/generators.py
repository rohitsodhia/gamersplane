import random
import math

from faker import Faker

from users.models import User

faker = Faker()
random_seed = math.floor(random.random() * 100000)
Faker.seed(random_seed)


class Generator:
    @staticmethod
    def user():
        user = User()
        user.name = faker.name()

        return user
