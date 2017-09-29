#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Conta quante volte una lettera si ripete in una parola

def ContaLettera(Stringa, Lettera, Posizione):
    if Posizione > len(Stringa)-1:
        return "Errore: la posizione e' maggiore della lunghezza della stringa"
    elif Posizione < 0:
        return "Errore: la posizione e' negativa"
    Conteggio = 0
    i = Posizione
    while i < len(Stringa):
        t = TrovaConta(Stringa, Lettera, Posizione) # Ritorna la posizione del carattere trovato
        if t >= 0: # Se e' vero allora e' stato trovato
            Conteggio = Conteggio + 1 # Tiene conto di quante volte e' stato trovato il carattere
        elif t < 0: # Se ritorna un numero < 0 allora non ci sono piu' caratteri da trovare
            return Conteggio
        i = i + 1
        Posizione = t + 1
    return Conteggio

def TrovaConta(Stringa, Lettera, Posizione):
    Indice = Posizione
    while Indice < len(Stringa):
        if Stringa[Indice] == Lettera:
            return Indice
        Indice = Indice + 1
    #print "Carattere non trovato"
    return -1

def main(args):
    print ContaLettera("Matteotti", "t", 0)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
