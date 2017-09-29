import random

def attacco():
    password = "5469"
    tentativo = 0
    while tentativo != password:
        tentativo = tentativo + 1
        #print tentativo
        if str(tentativo) == password:
            print "La password e': ", password
            return password

def main(args):
    attacco()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
