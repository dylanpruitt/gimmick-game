import pygame
from entities.entity import Entity, Player
from weapons.switcheroo import Switcheroo
from weapons.magnet import Magnet
from objects.kill_part import KillPart

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gimmick Game")


class Game:
    def __init__(self):
        self.looping = True
        self.player = Player(240, 240)
        self.player.weapons.append(Switcheroo())
        self.player.weapons.append(Magnet())
        self.entities = []
        self.entities.append(self.player)
        self.entities.append(Entity(100, 380))
        self.entities.append(Entity(300, 380))
        self.objects = []
        self.objects.append(KillPart(350, 100))
        self.clock = pygame.time.Clock()


game = Game()


def update_entity(entity):
    entity.x = round(entity.x + entity.dx)
    entity.y = round(entity.y + entity.dy)
    if entity.dx > 0:
        entity.dx -= 0.3
    if entity.dx < 0:
        entity.dx += 0.3
    if entity.dy > 0:
        entity.dy -= 0.3
    if entity.dy < 0:
        entity.dy += 0.3
    for object in game.objects:
        if entity.is_colliding_with(object):
            object.on_touch(entity)

    render_entity(entity)


def render_entity(entity):
    COLOR = (0, 0, 0)
    if entity.isPlayer:
        COLOR = WHITE
    else:
        COLOR = RED
    pygame.draw.rect(screen, COLOR, (entity.x, entity.y, entity.width, entity.height))
    

def update_object(object):
    object.x = round(object.x + object.dx)
    object.y = round(object.y + object.dy)
    if object.dx > 0:
        object.dx -= 0.3
    if object.dx < 0:
        object.dx += 0.3
    if object.dy > 0:
        object.dy -= 0.3
    if object.dy < 0:
        object.dy += 0.3
    render_object(object)
    
    
def render_object(object):
    pygame.draw.rect(screen, object.color, (object.x, object.y, object.width, object.height))


def loop():
    keys_held = []

    while game.looping:
        game.clock.tick(30)

        screen.fill(BLACK)

        font = pygame.font.Font(None, 30)
        text = font.render("1: Switcheroo", 1, RED)
        screen.blit(text, (15, 15))

        text = font.render("2: Magnet", 1, RED)
        screen.blit(text, (15, 35))

        temp_entities = []
        for entity in game.entities:
            update_entity(entity)
            if entity.health > 0:
                temp_entities.append(entity)

        game.entities = temp_entities

        for object in game.objects:
            update_object(object)

        pygame.display.flip()

        for key in keys_held:
            if key == "up":
                game.player.dy -= game.player.move_speed
            if key == "left":
                game.player.dx -= game.player.move_speed
            if key == "down":
                game.player.dy += game.player.move_speed
            if key == "right":
                game.player.dx += game.player.move_speed
            if key == "2":
                game.player.weapons[1].use(game.player, game.entities)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.looping = False
                if event.key == pygame.K_UP:
                    keys_held.append("up")
                if event.key == pygame.K_LEFT:
                    keys_held.append("left")
                if event.key == pygame.K_DOWN:
                    keys_held.append("down")
                    game.player.dy += game.player.move_speed
                if event.key == pygame.K_RIGHT:
                    keys_held.append("right")
                    game.player.dx += game.player.move_speed
                if event.key == pygame.K_1:
                    game.player.weapons[0].use(game.player, game.entities)
                if event.key == pygame.K_2:
                    keys_held.append("2")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    keys_held.remove("up")
                if event.key == pygame.K_LEFT:
                    keys_held.remove("left")
                if event.key == pygame.K_DOWN:
                    keys_held.remove("down")
                if event.key == pygame.K_RIGHT:
                    keys_held.remove("right")
                if event.key == pygame.K_2:
                    keys_held.remove("2")

loop()
pygame.quit()
