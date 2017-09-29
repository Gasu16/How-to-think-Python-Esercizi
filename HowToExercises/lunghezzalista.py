# Stampa la lunghezza di ogni elemento contenuto in una lista

Squadre = ["juventus", "milan"]

def funz(Squadre):
    i = 0
    while i < len(Squadre):
        #print Squadre[i]
        print len(Squadre[i])
        i = i + 1

def main(args):
    funz(Squadre)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
