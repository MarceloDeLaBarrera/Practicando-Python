from tkinter import *

root = Tk()
frame = Frame()
frame.pack()


def imprimir():
    print(varopcion.get())
    if varopcion.get() == 1:
        L2.config(text="Ha seleccionado el genero Masculino")
    elif varopcion.get() == 2:
        L2.config(text="Ha seleccionado el genero Femenino")
    else:
        return ""


L1 = Label(frame, text="Genero")
L1.pack()
varopcion = IntVar()
RB1 = Radiobutton(frame, text="Masculino",
                  variable=varopcion, value=1, command=imprimir)
RB2 = Radiobutton(frame, text="Femenino", variable=varopcion,
                  value=2, command=imprimir)
RB1.pack()
RB2.pack()

L2 = Label(frame)
L2.pack()


root.mainloop()
