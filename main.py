import pygame
from entities.entity import Entity, Player
from weapons.switcheroo import Switcheroo
from weapons.magnet import Magnet

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
    render_entity(entity)


def render_entity(entity):
    COLOR = (0, 0, 0)
    if entity.isPlayer:
        COLOR = WHITE
    else:
        COLOR = RED
    pygame.draw.rect(screen, COLOR, (entity.x, entity.y, entity.width, entity.height))


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

        for entity in game.entities:
            update_entity(entity)

        pygame.display.flip()

        for key in keys_held:
            if key == "w":
                game.player.dy -= game.player.move_speed
            if key == "a":
                game.player.dx -= game.player.move_speed
            if key == "s":
                game.player.dy += game.player.move_speed
            if key == "d":
                game.player.dx += game.player.move_speed
            if key == "2":
                game.player.weapons[1].use(game.player, game.entities)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.looping = False
                if event.key == pygame.K_w:
                    keys_held.append("w")
                if event.key == pygame.K_a:
                    keys_held.append("a")
                if event.key == pygame.K_s:
                    keys_held.append("s")
                    game.player.dy += game.player.move_speed
                if event.key == pygame.K_d:
                    keys_held.append("d")
                    game.player.dx += game.player.move_speed
                if event.key == pygame.K_1:
                    game.player.weapons[0].use(game.player, game.entities)
                if event.key == pygame.K_2:
                    keys_held.append("2")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys_held.remove("w")
                if event.key == pygame.K_a:
                    keys_held.remove("a")
                if event.key == pygame.K_s:
                    keys_held.remove("s")
                if event.key == pygame.K_d:
                    keys_held.remove("d")
                if event.key == pygame.K_2:
                    keys_held.remove("2")

loop()
pygame.quit()
