#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pendenza

import math

def getpendenza(x1, y1, x2, y2):
	m = (y2 - y1)/(x2 - x1)
	return m

def intercettaY(x1, y1, x2, y2):
	# y = mx + q (q e' l'intercetta)
	# b = y - mx
	b = y2 - getpendenza(x1, y1, x2, y2) * x2
	return b
	
	

def main(args):
	print(intercettaY(1.0, 2.0, 4.0, 6.0))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
