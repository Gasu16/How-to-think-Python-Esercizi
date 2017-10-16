import math
import copy

class Punto:
    x = 0.0
    y = 0.0

class Rettangolo:
    altezza = 0.0
    larghezza = 0.0
    x = 30
    y = 50

def distanza2punti(P1, P2):
    distanza = math.sqrt(((P2.x - P1.x) ** 2) + ((P2.y - P1.y) ** 2))
    print distanza
    return distanza

def stessoPunto(P1, P2):
    s = (P1.x == P2.x) and (P1.y == P2.y)
    print s
    return s

def trovaCentro(Rettangolo):
    P = Punto()
    P.x = Rettangolo.altoSinistra.x + Rettangolo.larghezza/2.0
    P.y = Rettangolo.altoSinistra.y + Rettangolo.altezza/2.0
    return P

def stampaPunto(Punto):
    print "Punto x: " + str(Punto.x)
    print "Punto y: " + str(Punto.y)

def muoviRettangolo(Rettangolo, dx, dy):
    Rettangolo.x += dx
    Rettangolo.y += dy
    print Rettangolo.x
    print Rettangolo.y

def newMuoviRettangolo(Rettangolo, dx, dy):
    R1 = copy.copy(Rettangolo)
    R1.x += dx
    R1.y += dy
    print R1.x
    print R1.y

def main(args):
    P1 = Punto()
    P2 = Punto()
    P1.x = 1.0
    P1.y = 2.0
    P2.x = 1.0
    P2.y = 2.0
    distanza2punti(P1, P2)
    stessoPunto(P1, P2)
    Rett = Rettangolo()
    Rett.largezza = 100.0
    Rett.altezza = 200.0
    Rett.altoSinistra = Punto()
    Rett.altoSinistra.x = 0.0
    Rett.altoSinistra.y = 0.0
    centro = trovaCentro(Rett)
    stampaPunto(centro)
    muoviRettangolo(Rett, 5, 5)
    newMuoviRettangolo(Rett, 10, 10)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

