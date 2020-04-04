from random import randint


class Die:
    def __init__(self, sides):
        if type(sides) is not int:
            raise TypeError("Sides must be an int")
        elif sides < 2:
            raise ValueError("Sides must be greater than 1")
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
