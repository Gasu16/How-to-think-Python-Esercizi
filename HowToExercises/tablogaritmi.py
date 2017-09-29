#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabelle logaritmi

import math

def logtm():
	x = 1.0
	while x <= 65536.0:
		print x, '\t', '\t', math.log(x, 2)
		x = x * 2.0

def main(args):
	logtm()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
