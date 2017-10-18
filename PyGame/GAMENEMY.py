import time
import datetime
import pygame
from pygame.locals import *
import random

class GameEnemy:

    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.pos.x = random.randrange(100, 400)
        self.pos.y = random.randrange(100, 300)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right >= 600:
            self.pos.left = 0

def main(args):
    bwidth = 640
    bheight = 480

    screen = pygame.display.set_mode((bwidth, bheight))
    quadrato = pygame.Surface((20, 20))
    quadrato.fill((255, 0, 0))
    background = pygame.Surface((bwidth, bheight))
    screen.blit(background, (0, 0))

    nemici = []
    for i in range(10):
        o = GameEnemy(quadrato, i*40, 10)
        nemici.append(o)
    while 1:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
        for o in nemici:
            screen.blit(background, o.pos, o.pos)
        for o in nemici:
            o.move()
            screen.blit(o.image, o.pos)

        pygame.display.update()
        pygame.time.delay(100)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
