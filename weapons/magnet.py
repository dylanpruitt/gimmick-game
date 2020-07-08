from weapons.weapon import Weapon


class Magnet(Weapon):
    def __init__(self):
        self.name = "Magnet"
        self.cooldown = 0
        self.attraction_force = 0.7

    def use(self, user, targets):
        for target in targets:
            if not (user.x == target.x and user.y == target.y):
                if user.x > target.x:
                    target.dx += self.attraction_force
                if user.x < target.x:
                    target.dx -= self.attraction_force
                if user.y > target.y:
                    target.dy += self.attraction_force
                if user.y < target.y:
                    target.dy -= self.attraction_force