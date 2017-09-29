#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conto alla rovescia

def contoAllaRovescia(n):
	while n >= 0:
		print n
		n -= 1

def main(args):
	contoAllaRovescia(5)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
