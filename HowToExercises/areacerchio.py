#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Area del cerchio

import math

def distanzaTra2Punti2(x1, y1, x2, y2):
	distanza = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
	return distanza

def AreaDelCerchio(Raggio):
	temp = math.pi * Raggio**2
	print temp
	return temp

def main(args):
	Raggio = distanzaTra2Punti2(1, 2, 4, 6)
	AreaDelCerchio(Raggio)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
