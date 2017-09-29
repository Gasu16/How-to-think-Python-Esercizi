#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  porzioni di stringhe


def main(args):
    frutto = "banana"
    parola = "ciao"
    if parola < frutto:
        print "", parola, " viene prima di ", frutto
    elif parola > frutto:
        print "", parola, " viene dopo ", frutto 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
