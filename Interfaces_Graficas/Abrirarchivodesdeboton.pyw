from tkinter import *
from tkinter import filedialog


root = Tk()
frame = Frame()
frame.pack()
root.title("Menu")
root.geometry("720x480")


def abrefichero():
    fichero = filedialog.askopenfile(
        title="Abrir", initialdir="C:\\", filetypes=(("Ficheros Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)


botonAbrir = Button(frame, text="Abrir", command=abrefichero)
botonAbrir.pack()

root.mainloop()
