from objects.object import Object


class KillPart(Object):
    def __init__(self, x, y):
        super(KillPart, self).__init__(x, y)
        self.color = (0, 0, 255)

    def on_touch(self, entity):
        entity.health -= 1
