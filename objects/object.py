class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.color = (128, 128, 128)
        self.width = 20
        self.height = 20
        self.move_speed = 0.5

    def on_touch(self, entity):
        pass