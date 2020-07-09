class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.health = 1
        self.width = 20
        self.height = 20
        self.move_speed = 0.5
        self.isPlayer = False


class Player(Entity):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y)
        self.isPlayer = True
        self.weapons = []
