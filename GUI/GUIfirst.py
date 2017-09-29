from Tkinter import *

root = Tk()

mioframe = Frame(root, width = 640, height = 480)
mioframe.pack()

pulsante1 = Button(mioframe, width = 15, height = 10)
pulsante1["text"] = "Ciao, prova"
pulsante1["background"] = "green"
pulsante1.pack()

root.mainloop()