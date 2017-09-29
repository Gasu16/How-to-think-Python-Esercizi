#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  compreso tra x y z (y < x < z)

def compresotra(x, y, z):
	if y <= x <= z: return 1
	else: return 0

def main(args):
	print(compresotra(2, 1, 3))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
