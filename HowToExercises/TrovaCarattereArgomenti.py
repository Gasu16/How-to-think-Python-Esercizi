#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Trova un carattere in una stringa

def Trova(Stringa, Carattere, Inizio = 0, Fine = 0):
    Fine = len(Stringa)
    if Inizio > len(Stringa)-1:
        return "Errore: la posizione e' maggiore della lunghezza della stringa"
    elif Inizio < 0:
        return "Errore: la posizione e' negativa"
    Indice = Inizio
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere:
            return Indice
        Indice = Indice + 1
    print "Carattere non trovato"
    return -1

def main(args):
    print Trova("ciao", "i", 0, 3)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
