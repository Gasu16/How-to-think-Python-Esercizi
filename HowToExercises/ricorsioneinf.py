#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ricorsione infinita

def ricorsione():
	ricorsione()

def main(args):
	ricorsione()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
