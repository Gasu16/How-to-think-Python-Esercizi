#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  concatenamento

def concatena():
    Prefissi = "JKLMNOPQ"
    Suffissi = "ack"
    for Lettera in Prefissi:
        if Lettera == "O" or Lettera == "Q":
            Suffissi = "uack"
        else:
            Suffissi = "ack" # l'else e' necessario in quanto la variabile Suffissi una volta raggiunta la O 
                             # si trasformerebbe in uack definitivamente, invece usando l'else si trasforma in uack 
                             # e successivamente ritorna in ack
        print Lettera + Suffissi

def main(args):
    concatena()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
