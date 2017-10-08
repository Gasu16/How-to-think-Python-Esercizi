import time
import datetime
import pygame
from pygame.locals import *
import random

enemyList = []
width = 640
height = 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
cond = True
x = random.randrange(0, 400)
y = random.randrange(0, 100)
rand = random.randrange(0, 10)

while cond:

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))

    screen.fill((255, 242, 0), (x, y, 20, 20))

    """for i in range(50):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = random.randrange(0, 400)
        y = random.randrange(0, 100)
        pygame.draw.rect(screen, (r, g, b), (x, y, 10, 10))"""

    y += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)