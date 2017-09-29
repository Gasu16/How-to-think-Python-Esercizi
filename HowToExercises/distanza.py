#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  distanza tra due punti

import math

def distanzaTra2Punti(x1, y1, x2, y2):
	distanza = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
	print distanza
	return distanza

def main(args):
	distanzaTra2Punti(1, 2, 4, 6)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

