from Tkinter import *

class MiaApp:
    def __init__(self, mioGenitore):
        self.mioContenitore1 = Frame(mioGenitore)
        self.mioContenitore1.pack()

        # Costruiamo il pulsante 1
        self.pulsante1 = Button(self.mioContenitore1, width = 25, height = 10)
        self.pulsante1.configure(text = "Pulsante 1", background = "green")
        self.pulsante1.pack()

        #Costruiamo il pulsante 2
        self.pulsante2 = Button(self.mioContenitore1, width = 25, height = 10)
        self.pulsante2.configure(text = "Pulsante 2", background = "yellow")
        self.pulsante2.pack()

        #Costruiamo il pulsante 3
        self.pulsante3 = Button(self.mioContenitore1, width = 25, height = 10)
        self.pulsante3.configure(text = "Pulsante 3", background = "cyan")
        self.pulsante3.pack()

root = Tk()
miaApp = MiaApp(root)
root.mainloop()
