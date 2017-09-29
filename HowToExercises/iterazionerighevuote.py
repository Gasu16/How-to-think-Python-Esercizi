#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  righevuoteiterazione

def NrigheVuote(n):
	while n > 0:
		print()
		n -= 1

def main(args):
	NrigheVuote(3)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
