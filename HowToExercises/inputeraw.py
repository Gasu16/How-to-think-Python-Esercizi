#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  input programma (input + raw_input)

def inserisciIntero():
	Prompt = "Inserisci un intero: "
	x = input(Prompt)
	print x

def inserisciStringa():
	x = raw_input("Inserisci stringa: ")
	print x

def main(args):
	inserisciIntero()
	inserisciStringa()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
