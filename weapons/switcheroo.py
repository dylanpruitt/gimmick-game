from weapons.weapon import Weapon
from random import randint


class Switcheroo(Weapon):
    def __init__(self):
        self.name = "Switcheroo"
        self.cooldown = 100

    def use(self, user, targets):
        random = randint(0, len(targets) - 1)

        temp_x = targets[random].x
        temp_y = targets[random].y
        targets[random].x = user.x
        targets[random].y = user.y
        user.x = temp_x
        user.y = temp_y
