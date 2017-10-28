import time
import datetime
import pygame
from pygame.locals import *
import random
"""
NEXT STEP: GESTIRE LE COLLISIONI
"""
# Classe del nemico
class GameEnemy:

    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()
        self.pos.x = random.randrange(10, 600)
        self.pos.y = random.randrange(10, 100)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right >= 600:
            self.pos.left = 0

# Classe del giocatore
class GamePlayer:
    def __init__(self, Rimage, Rheight, Rspeed):
        self.Rspeed = Rspeed
        self.Rimage = Rimage
        self.Rpos = Rimage.get_rect()
        self.Rpos.x = 250
        self.Rpos.y = 300

    def move(self):
        # Gestiamo i movimenti del rettangolo
        key = pygame.key.get_pressed()
        dist = 10

        if key[pygame.K_LEFT]:
            self.Rpos.x -= dist
        if key[pygame.K_RIGHT]:
            self.Rpos.x += dist
        if key[pygame.K_UP]:
            self.Rpos.y -= dist
        if key[pygame.K_DOWN]:
            self.Rpos.y += dist

    def screenCollision(self):
        if self.Rpos.x <= 0 or self.Rpos.y >= 430 or self.Rpos.x >= 540 or self.Rpos.y <= 0:
            return True

        #return self.rect.colliderect(GamePlayer.rect)

def main(args):
    bwidth = 640
    bheight = 480

    # Creiamo la scritta per quando si perde
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans", 30)
    # render text
    label = myfont.render("HAI PERSO", 1, (255, 0, 0))


    # Creiamo lo schermo e i nemici
    screen = pygame.display.set_mode((bwidth, bheight))
    quadrato = pygame.Surface((20, 20))
    quadrato.fill((255, 0, 0))

    # Creiamo il giocatore
    rettangolo = pygame.Surface((100, 50))
    rettangolo.fill((120, 0, 88))
    r = GamePlayer(rettangolo, 50, 10)

    # Creiamo il background
    background = pygame.Surface((bwidth, bheight))
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    nemici = []

    for i in range(10):
        o = GameEnemy(quadrato, i*40, 10)
        nemici.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background, r.Rpos, r.Rpos) # Disegniamo lo sfondo
        r.move() # Permettiamo al giocatore di muoversi
        screen.blit(r.Rimage, r.Rpos) # Ridisegniamo ogni volta lo sfondo per evitare di creare la "scia"

        for o in nemici:
            screen.blit(background, o.pos, o.pos) # Ridisegniamo ogni volta lo sfondo


        for o in nemici:
            o.move() # Muoviamo i nemici
            screen.blit(o.image, o.pos) # Disegniamo i nemici
            #pygame.time.delay(100)
            #pygame.display.update()
        print "X: " + str(r.Rpos.x)
        print "Y: " + str(r.Rpos.y)
        if r.screenCollision():
            screen.blit(label, (100, 100))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(240)
        pygame.time.delay(100)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
