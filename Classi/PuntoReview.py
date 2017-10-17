# Rivisita della classe Punto con ridefinizione degli operatori tramite metodi

class Punto:

    # Metodo per inizializzare la classe Punto
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Metodo per stampare a video in formato stringa
    def __str__(self):
        return "X: " + str(self.x) + ", Y: " + str(self.y)

    # Metodo per aggiungere
    def __add__(self, newPunto):
        return Punto(self.x + newPunto.x, self.y + newPunto.y)

    # Metodo per sottrarre
    def __sub__(self, newPunto):
        return Punto(self.x - newPunto.x, self.y - newPunto.y)

def main(args):
    P = Punto(3, 5)
    P2 = Punto(2, 2)
    Addizione = P.__add__(P2)
    print "Addizione: " + Addizione.__str__()
    Sottrazione = P.__sub__(P2)
    print "Sottrazione: " + Sottrazione.__str__()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
