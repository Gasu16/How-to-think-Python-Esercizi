# Liste

def nuovaLista(argomento):
    L = [argomento]
    return L

def main(args):
    print nuovaLista([3, 2, 6])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
