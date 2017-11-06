import time
import datetime
import pygame
from pygame.locals import *
import random
import inputbox
"""
NEXT STEP: 
1 - USCIRE PREMENDO ESCAPE 
Ultima modifica: [06/11/2017]
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


def main(args):
    bwidth = 640 # background width
    bheight = 480 # background height

    # Aggiungiamo la musica di sottofondo
    #pygame.init()
    #pygame.mixer.music.load("TheProdigy1.mp3")
    #pygame.mixer.music.play()

    # Creiamo la scritta per quando si perde
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans", 30)
    label = myfont.render("HAI PERSO", 1, (255, 0, 0))

    # Creiamo la scritta per il menu'
    menu_message = myfont.render("FALLING BOX", 1, (0, 255, 34))
    menu_easy = myfont.render("1 - FACILE", 1, (255, 255, 255))
    menu_regular = myfont.render("2 - DIFFICILE", 1, (255, 255, 255))
    menu_exit = myfont.render("0 - ESCI", 1, (0, 0, 255))

    # Creiamo lo schermo e i nemici
    screen = pygame.display.set_mode((bwidth, bheight))
    quadrato = pygame.Surface((20, 20))
    EnemyRed = random.randint(10, 255)
    EnemyGreen = random.randint(40, 222)
    EnemyBlue = random.randint(10, 200)
    quadrato.fill((EnemyRed, EnemyGreen, EnemyBlue))

    # Creiamo il menu' e scegliamo la difficolta'
    # N.B.: cambiare anche la velocita' quando si cambia difficolta')
    screen.blit(menu_message, (200, 100))
    screen.blit(menu_easy, (200, 300))
    screen.blit(menu_regular, (200, 350))
    screen.blit(menu_exit, (200, 400))

    while 1:
        scelta = inputbox.ask(screen, "SCELTA")
        if scelta == str(0):
            return 0
        if scelta == str(1):
            # Modalita' facile: 10 nemici
            numNem = 10
            speedspawn = random.randint(0, 5)
            break
        if scelta == str(2):
            # Modalita' difficile: 50 nemici
            numNem = 50
            speedspawn = random.randint(0, 10)
            break
        if scelta != str(0) and scelta != str(1) and scelta != str(2):
            scelta = inputbox.ask(screen, "SCELTA")

    # Creiamo il giocatore
    rettangolo = pygame.Surface((10, 30))
    rettangolo.fill((120, 0, 88))
    r = GamePlayer(rettangolo, 50, 10)

    # Creiamo il background
    background = pygame.Surface((bwidth, bheight))
    screen.blit(background, (0, 0))
    clock = pygame.time.Clock()
    nemici = []


    for i in range(numNem):
        o = GameEnemy(quadrato, i*40, 10)
        nemici.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_f:
                pass

        screen.blit(background, r.Rpos, r.Rpos) # Disegniamo lo sfondo
        r.move() # Permettiamo al giocatore di muoversi
        screen.blit(r.Rimage, r.Rpos) # Ridisegniamo ogni volta lo sfondo per evitare di creare la "scia"

#        for o in nemici:
#            screen.blit(background, o.pos, o.pos) # Ridisegniamo ogni volta lo sfondo

        for o in nemici:
            speedspawn = random.randint(0, len(nemici))
            # Piu' e' probabile che la condizione if sia vera, piu' veloci saranno i nemici
            if speedspawn >= 5:
                screen.blit(background, o.pos, o.pos)  # Ridisegniamo ogni volta lo sfondo
                o.move() # Muoviamo i nemici
                screen.blit(o.image, o.pos)  # Disegniamo i nemici
            if o.pos.colliderect(r.Rpos):
                screen.blit(label, (100, 100))

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
