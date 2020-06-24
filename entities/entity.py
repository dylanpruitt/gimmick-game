class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.health = 1
        self.width = 20
        self.height = 20
        self.move_speed = 1
        self.isPlayer = False
