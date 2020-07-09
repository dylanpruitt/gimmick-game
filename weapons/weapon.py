class Weapon:
    name = "default"
    cooldown = 100

    def __init__(self):
        pass

    def use(self, user, targets):
        raise NotImplementedError("not implemented")