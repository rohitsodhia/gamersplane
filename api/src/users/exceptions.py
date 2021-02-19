class UserExists(Exception):
    def __init__(self, errors) -> None:
        self.errors = errors
        super().__init__("User already exists")
