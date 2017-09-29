#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fattoriale

def fattoriale(n):
	if type(n) != type(1):
		print "Errore: " + str(n) + " non e' un numero intero"
	elif n < 0:
		print "Errore: " + str(n) + " e' minore di 0"
	elif n == 0 or n == 1:
		return 1
	else:
		return n * fattoriale(n-1)

def main(args):
	print(fattoriale(3))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
