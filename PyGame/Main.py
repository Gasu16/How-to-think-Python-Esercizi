# Creiamo la mappa
import time
from datetime import *
import pygame
from pygame.locals import *
import random

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
color = random.randint(0, 255)

red = 255
green = 0
blue = 0
x = 270
y = 225
xb = x
yb = y

while running:

    key = pygame.key.get_pressed()
    dist = 1
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_RIGHT]:
        x += 1
    if key[pygame.K_UP]:
        y -= 1
    if key[pygame.K_DOWN]:
        y += 1

    #screen = pygame.display.set_mode((width, height))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 640, 480))
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 620, 460))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 50))
    if xb != x and yb != y:
        xb = x
        yb = y
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 50))
    if x > 530 or y > 420 or x < 10 or y < 10:
        x = 270
        y = 225
        pygame.draw.rect(screen, (255, 0, 0), (270, 225, 100, 50))
    #screen.set_at((x, y), (red, green, blue))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    pygame.display.flip()
    clock.tick(240)
