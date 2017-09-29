#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classificazione caratteri

import string

def main(args):
    print string.lowercase # lettere minuscole
    print string.uppercase # Lettere maiuscole
    print string.digits # cifre da 0 a 9
    print string.whitespace # tutti gli spazi bianchi inclusi tabulazione (\t) e ritorno a capo (\n)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
