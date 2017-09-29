#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  confronto

def confronto(x, y):
	if x < y: return -1
	if x > y: return 1
	if x == y: return 0

def main(args):
	print(confronto(3, 2))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
