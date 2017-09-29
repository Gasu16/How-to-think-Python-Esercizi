#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Elaborazione trasversale di una stringa (al contrario)

def attraversamento(Stringa):
    i = len(Stringa) - 1 # Mettiamo l'indice i all'ultimo carattere della stringa
    while i >= 0: # Scorriamo l'indice dall'ultimo carattere al primo
        print Stringa[i]
        i -= 1

def main(args):
    attraversamento("ciao")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
