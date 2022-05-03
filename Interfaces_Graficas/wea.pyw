"""from tkinter import Tk, Label
# rw = row | cl = column
raiz = Tk()
for rw in range(4):
    for cl in range(8):
        Label(raiz, text=' (Row %s) \n (Column = %s) ' % (rw, cl),
              borderwidth=15).grid(row=rw, column=cl)
raiz.mainloop()"""

from tkinter import *

raiz = Tk()
frame = Frame(raiz)
frame.pack()
calculo_pantalla = StringVar()
calculo_pantalla.set("0")

PreAns = 0
Ans = 0
calculo_actual = 0
funcion = ""


######################################################################        GENERADOR BOTONES        ######################################################################


class boton():

    def __init__(self, caracter, fila, columna):
        self.caracter = caracter
        self.fila = fila
        self.columna = columna
        self.__genera_boton()

    def __genera_boton(self):
        self.boton = Button(frame, text=self.caracter, width=8,
                            height=4, command=lambda: funcion_pantalla(self.caracter))
        self.boton.grid(row=self.fila, column=self.columna)


######################################################################       FUNCION DE CADA BOTON       ######################################################################

def funcion_pantalla(caracter):
    global Ans, funcion, calculo_actual

#	prueba=  float(calculo_pantalla.get())  <--- Intento de hacer que después de cada signo de operacion se muestre el resultado

    if caracter == "+":
        calculo_actual += float(calculo_pantalla.get())
        calculo_pantalla.set("")
        funcion = "+"

    elif caracter == "-":
        if funcion == "-":
            calculo_actual -= float(calculo_pantalla.get())
            calculo_pantalla.set("")
        else:
            calculo_actual += float(calculo_pantalla.get())
            calculo_pantalla.set("")
            funcion = "-"

    elif caracter == "x":
        if funcion == "x":
            calculo_actual *= float(calculo_pantalla.get())
            calculo_pantalla.set("")
        else:
            calculo_actual += float(calculo_pantalla.get())
            calculo_pantalla.set("")
            funcion = "x"

    elif caracter == "/":
        if funcion == "/":
            calculo_actual /= float(calculo_pantalla.get())
            calculo_pantalla.set("")
        else:
            calculo_actual += float(calculo_pantalla.get())
            calculo_pantalla.set("")
            funcion = "/"

    elif caracter == "=":
        if funcion == "+":
            calculo_actual += float(calculo_pantalla.get())
            calculo_pantalla.set(str(calculo_actual))
        elif funcion == "-":
            calculo_actual -= float(calculo_pantalla.get())
            calculo_pantalla.set(str(calculo_actual))

        elif funcion == "x":
            calculo_actual *= float(calculo_pantalla.get())
            calculo_pantalla.set(str(calculo_actual))

        elif funcion == "/":
            calculo_actual /= float(calculo_pantalla.get())
            calculo_pantalla.set(str(calculo_actual))

        funcion = ""
        PreAns = Ans
        Ans = calculo_actual
        calculo_actual = 0

    elif calculo_pantalla.get() != "0" and calculo_pantalla.get() == str(Ans):
        calculo_pantalla.set(str(caracter))

    elif calculo_pantalla.get() != "0":
        calculo_pantalla.set(calculo_pantalla.get() + str(caracter))

    elif calculo_pantalla.get() == "0" and str(caracter) != "0":
        calculo_pantalla.set(str(caracter))
    else:
        pass


pantalla = Entry(frame, bg="grey", fg="white", justify="right",
                 font=30, textvariable=calculo_pantalla)
pantalla.grid(row=0, column=0, columnspan=4, sticky="we")


######################################################################       CREAR BOTONES       ######################################################################

lista_botones = [7, 8, 9, "/", 4, 5, 6, "x", 1, 2, 3, ".", "+", 0, "-", "="]
diccionario_botones = {}
selector = 0

for i in lista_botones:
    diccionario_botones["boton_" +
                        str(i)] = boton(i, selector // 4 + 1, selector % 4)
    selector += 1

raiz.mainloop()
