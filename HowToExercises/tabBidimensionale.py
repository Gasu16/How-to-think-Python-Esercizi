#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabellabidimensionale

def StampaMultipli(n, Grandezza):
	i = 1
	while i <= Grandezza:
		print n*i, '\t',
		i = i + 1
	print
	
def TabellaMoltiplicazioneGenerica(Grandezza):
	i = 1
	while i <= Grandezza:
		StampaMultipli(i, Grandezza)
		i = i + 1

def main(args):
	TabellaMoltiplicazioneGenerica(7)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
