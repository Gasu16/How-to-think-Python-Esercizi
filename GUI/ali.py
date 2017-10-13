from Tkinter import *
import tkinter as tk
import tkinter.messagebox
from math import sin, pi

def calcola(n):
    if n < 2:
        return tk.messagebox.showerror("Errore", "Inserisci un valore maggiore o uguale a 2")
    f = lambda x: x * sin(x)
    a = 0
    b = pi / 2

    h = (b - a) / n
    s = 0.05 * (f(a) + f(b))
    for i in range(1, n):
        s += f(i * h)
        y = h * s
    return tk.messagebox.showinfo("Risultato", y)


def main(args):
    root = tk.Tk()
    var = IntVar() # Integer value input
    e = tk.Entry(root, textvariable = var, width = 20) # Where we catch the value
    e.pack()
    var.set(e.get()) # Set the value of var
    L1 = tk.Label(root, width = 50, height = 10)
    L1.pack()
    b = tk.Button(root, command = lambda: calcola(var.get()), text = "Calcola!") # Button to calculate
    b.pack()
    root.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
