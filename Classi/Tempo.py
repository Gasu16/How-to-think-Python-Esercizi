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

def sommaTempo(T1, T2):
    Secondi = ConverteInSecondi(T1) + ConverteInSecondi(T2)
    return ConverteInTempo(Secondi)

def Dopo(T1, T2):
    if T1 >= T2:
        return True
    else:
        return False

def Incremento(Tempo, Secondi):
    Tempo.secondi += Secondi
    while Tempo.secondi >= 60:
        Tempo.secondi -= 60
        Tempo.minuti += 1
    while Tempo.minuti >= 60:
        Tempo.minuti -= 60
        Tempo.ore += 1

def newIncremento(Tempo, Secondi):
    while ConverteInSecondi(Tempo) >= 60:
        return ConverteInSecondi(Tempo)

#### CONVERTE UN OGGETTO TEMPO IN SECONDI ####
def ConverteInSecondi(Tempo):
    minuti = Tempo.ore * 60 + Tempo.minuti
    secondi = Tempo.minuti * 60 + Tempo.secondi
    return secondi

#### CONVERTE I SECONDI IN UN OGGETTO TEMPO ####
def ConverteInTempo(Secondi):
    T = Tempo()
    T.ore = Secondi/3600
    Secondi = Secondi - T.ore * 3600
    T.minuti = Secondi/60
    Secondi = Secondi - T.minuti * 60
    T.secondi = Secondi
    return T

def main(args):
    Time = Tempo()
    tempo1 = Tempo()
    tempo2 = Tempo()
    setTempo(23, 35, 40)
    print stampaTempo(Time)
    print stampaTempo(sommaTempo(tempo1, tempo2))
    print newIncremento(Time, 10)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))