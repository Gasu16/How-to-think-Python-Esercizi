class Rettangolo:
    larghezza = 0
    altezza = 0

def main(args):
    Rett = Rettangolo()
    Rett.largezza = 100
    Rett.altezza = 200
    print Rett.altezza
    print Rett.largezza
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
