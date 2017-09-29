#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minuscolo
import string
from datetime import datetime

def Minuscolo1(Carattere):
    return string.find(string.lowercase, Carattere) != -1
    
def Minuscolo2(Carattere):
    return Carattere in string.lowercase

def Minuscolo3(Carattere):
    return 'a' <= Carattere <= 'z'

def main(args):
    startTime = datetime.now()
    # Minuscolo1 = 0000.24
    # Minuscolo2 = 0000.29
    # Minuscolo3 = 0000.24
    Minuscolo3('c')
    print datetime.now() - startTime
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
