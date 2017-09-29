#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Trova un carattere in una stringa

def Trova(Stringa, Carattere, Posizione):
    if Posizione > len(Stringa)-1:
        return "Errore: la posizione e' maggiore della lunghezza della stringa"
    elif Posizione < 0:
        return "Errore: la posizione e' negativa"
    Indice = Posizione
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere:
            return Indice
        Indice = Indice + 1
    print "Carattere non trovato"
    return -1

def main(args):
    print Trova("ciao", "c", 44)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
