import pygame
from entities.entity import Entity
from weapons.switcheroo import Switcheroo

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gimmick Game")


class Game:
    def __init__(self):
        self.looping = True
        self.player = Entity(240, 240)
        self.player.isPlayer = True
        self.test_enemy = Entity(100,380)
        self.switcheroo = Switcheroo()
        self.clock = pygame.time.Clock()


game = Game()


def update_entity(entity):
    entity.x = round(entity.x + entity.dx)
    entity.y = round(entity.y + entity.dy)
    render_entity(entity)


def render_entity(entity):
    COLOR = (0, 0, 0)
    if entity.isPlayer:
        COLOR = WHITE
    else:
        COLOR = RED
    pygame.draw.rect(screen, COLOR, (entity.x, entity.y, entity.width, entity.height))


def loop():
    while game.looping:
        game.clock.tick(30)

        while game.looping:
            screen.fill(BLACK)

            font = pygame.font.Font(None, 75)
            text = font.render(str(pygame.time.get_ticks()), 1, RED)
            screen.blit(text, (150, 150))

            update_entity(game.player)
            update_entity(game.test_enemy)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.looping = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.looping = False
                    if event.key == pygame.K_w:
                        game.player.dy -= game.player.move_speed
                    if event.key == pygame.K_a:
                        game.player.dx -= game.player.move_speed
                    if event.key == pygame.K_s:
                        game.player.dy += game.player.move_speed
                    if event.key == pygame.K_d:
                        game.player.dx += game.player.move_speed
                    if event.key == pygame.K_1:
                        targets = []
                        targets.append(game.player)
                        targets.append(game.test_enemy)
                        game.switcheroo.use(game.player, targets)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        game.player.dy = 0
                    if event.key == pygame.K_a:
                        game.player.dx = 0
                    if event.key == pygame.K_s:
                        game.player.dy = 0
                    if event.key == pygame.K_d:
                        game.player.dx = 0


loop()
pygame.quit()
