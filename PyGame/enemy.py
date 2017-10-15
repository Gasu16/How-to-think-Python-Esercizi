import time
import datetime
import pygame
from pygame.locals import *
import random


width = 640
height = 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pl = pygame.Surface((20, 20))
pl.fill((255, 242, 0))
background = pygame.Surface((width, height))
screen.blit(background, (0, 0))        #draw the background
posizione = pl.get_rect()
screen.blit(pl, posizione)          #draw the player
cond = True
pygame.display.update()

while cond:
    screen.blit(background, posizione, posizione)
    posizione = posizione.move(0, 5)
    screen.blit(pl, posizione)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False

    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)