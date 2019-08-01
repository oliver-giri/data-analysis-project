import pygame, sys, pandas as pd
from rock import Rock
from ship import Ship

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
import random

info = pd.read_csv("data.csv")
numlevels = info["level"].max()
level = info["level"].min()
levelInfo = info.iloc[level]
rocks = []
player = Ship(20, 250)

def init():
    global rocks, player, levelInfo
    player.x = 20
    player.y = 250
    rocks = []
    levelInfo = info.iloc[level]
    for i in range(levelInfo["numRock"]):
        rocks.append(Rock(random.randint(300, 500), random.randint(200, 300), random.randint(-5, 5), random.randint(-5, 5), random.randint(10, 50)))

init()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.yVelocity -= Ship.speed
            if event.key == pygame.K_s:
                player.yVelocity += Ship.speed
            if event.key == pygame.K_a:
                player.xVelocity -= Ship.speed
            if event.key == pygame.K_d:
                player.xVelocity += Ship.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.yVelocity += Ship.speed
            if event.key == pygame.K_s:
                player.yVelocity -= Ship.speed
            if event.key == pygame.K_a:
                player.xVelocity += Ship.speed
            if event.key == pygame.K_d:
                player.xVelocity -= Ship.speed
    pygame.draw.polygon(screen, (255, 0, 0), [[player.x - Ship.size/2, player.y + Ship.size/2],
                                              [player.x + Ship.size/2, player.y],
                                              [player.x - Ship.size/2, player.y - Ship.size/2]], 0)
    player.move()
    for rock in rocks:
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(rock.x, rock.y, rock.size, rock.size), 0)
        rock.move()
        rock.bounce()
    if player.y > rock.y and player.y < rock.y + rock.size and player.x > rock.x and player.x < rock.x + rock.size:
        init()
    if player.x > 900:
        level += 1
        if level > numlevels:
            break
        init()
    pygame.display.flip()
    screen.fill((0,0,0))
