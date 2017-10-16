class Tempo:
    ore = 0
    minuti = 0
    secondi = 0

def setTempo(ore, minuti, secondi):
    Tempo.ore = ore
    Tempo.minuti = minuti
    Tempo.secondi = secondi


def stampaTempo(Tempo):
    return "" + str(Tempo.ore) + ":" + str(Tempo.minuti) + ":" + str(Tempo.secondi)

def Dopo(T1, T2):
    if T1 >= T2:
        return True
    else:
        return False

def main(args):
    Time = Tempo()
    setTempo(23, 35, 40)
    print stampaTempo(Time)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))