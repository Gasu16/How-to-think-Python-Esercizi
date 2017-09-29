# ---- compito 2:  definizione del codice di gestione degli eventi
def gestisci_A():
    print "Sbagliato! Prova ancora!"


def gestisci_B():
    print "Bravissimo! Il ranuncolo e' un fiore!"


def gestisci_C():
    print "Sbagliato! Prova ancora!"


# ---- compito 1: definizione dell'aspetto sullo schermo
print "\n" * 100  # pulisci lo schermo
print "             UN QUIZ ESTREMAMENTE APPASSIONANTE"
print "==========================================================="
print "Premere il tasto corrispondente alla risposta, poi [Invio]."
print
print "    A.  Animale"
print "    B.  Vegetale"
print "    C.  Minerale"
print
print "    X.  Termina questo programma"
print
print "==========================================================="
print "Che cos'e' un 'Ranuncolo'?"
print

# ---- compito 4: ciclo degli eventi. Ciclo infinito, in attesa di eventi
while 1:

    # Osserva il successivo ingresso
    risposta = raw_input().upper()

    # ---------------------------------------------------------
    # compito 3: associare eventi della tastiera 'interessanti'
    # con i gestori di eventi. Una semplice forma di
    # collegamento
    # ---------------------------------------------------------
    if risposta == "A":
        gestisci_A()
    if risposta == "B":
        gestisci_B()
    if risposta == "C":
        gestisci_C()
    if risposta == "X":
        # pulisce lo schermo e termina il ciclo degli eventi
        print "\n" * 100
        break

        # Si noti che tutti gli altri eventi sono giudicati non
        # interessanti, e percio` ignorati