from tkinter import *

root = Tk()
frame = Frame()
frame.pack()

varplaya = IntVar()
varmontana = IntVar()
varbosque = IntVar()


def seleccion():
    opcionEscogida = ""
    if varplaya.get() == 1:
        opcionEscogida += " Ha escogido Playa"
    if varmontana.get() == 1:
        opcionEscogida += " Ha escogido Montaña"
    # elif varbosque.get() == 1:
    if varbosque.get() == 1:
        opcionEscogida += " Ha escogido Bosque"
    # else:
     #   opcionEscogida += ""

    LB3.config(text=opcionEscogida)


foto = PhotoImage(
    file="D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\avion.png")
LB1 = Label(frame, image=foto)
LB1.pack()

LB2 = Label(frame, text="Elige destino", width=50)
LB2.pack()

# onvalue cuando esta seleccionado
CB1 = Checkbutton(text="Playa", variable=varplaya,
                  onvalue=1, offvalue=0, command=seleccion)
CB1.pack()
CB2 = Checkbutton(text="Montaña", variable=varmontana,
                  onvalue=1, offvalue=0, command=seleccion)
CB2.pack()
CB3 = Checkbutton(text="Bosque", variable=varbosque,
                  onvalue=1, offvalue=0, command=seleccion)
CB3.pack()

LB3 = Label(root)
LB3.pack()

root.mainloop()
