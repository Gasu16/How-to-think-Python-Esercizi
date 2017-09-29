#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logaritmi

import math

def logaritmo(n):
	return math.log(n) # calcola il logaritmo in base e

def logaritmobase10(n):
	return math.log10(n) # calcola il logaritmo in base 10

def logaritmobase2(n):
	return math.log(n, 2) # calcola il logaritmo in base 2

def main(args):
	print(logaritmo(4)) 
	print(logaritmobase10(4))
	print(logaritmobase2(4))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
