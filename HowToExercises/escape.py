#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  escape

def escfor():
	print "produca", '\n', '\t', "questo", '\n','\t', '\t', "risultato"

def main(args):
	escfor()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
