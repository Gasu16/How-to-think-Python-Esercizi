#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  righe vuote esercizio how to think

def TreRigheVuote():
	print()
	print()
	print()
	
def NoveRigheVuote():
	TreRigheVuote()
	TreRigheVuote()
	TreRigheVuote()

def righeVuote(i):
	for count in range(0, i):
		print()

def main(args):
    righeVuote(3)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
