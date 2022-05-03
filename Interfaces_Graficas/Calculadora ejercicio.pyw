from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

numeroPantalla = StringVar()
operacion = ""
resultado = 0
count = 0

reset_pantalla = False


# Pantalla

# colspan alias columspan permite extender un elemento a la cantidad de columnas que se le indique.
pantalla = Entry(frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=5, pady=5, columnspan=4)
pantalla.config(bg="Black", fg="#03f943", justify="right")

# Pulsaciones teclado.


def numeroPulsado(numerotecleado):
    global reset_pantalla

    # Si operacion es distinto de vacio, es decir, pulso boton operacion, no concadene, si no que escriba el nuevo numero tecleado. Ademas se debe volver a vaciar operacion, si no, se vaciara sin concadenar infinitamente.
    if reset_pantalla != False:
        numeroPantalla.set(numerotecleado)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + numerotecleado)


def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    operacion = "suma"
    resultado += float(num)
    numeroPantalla.set(resultado)
    reset_pantalla = True


def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    operacion = "resta"
    if resultado == 0:
        resultado = resultado + float(num)
        numeroPantalla.set(resultado)
        reset_pantalla = True
    else:
        resultado = resultado - float(num)
        numeroPantalla.set(resultado)
        reset_pantalla = True


def multi(num):
    global operacion
    global resultado
    operacion = "multi"
    resultado += float(num)
    numeroPantalla.set(resultado)


def div(num):
    global operacion
    global resultado
    operacion = "div"
    resultado += float(num)
    numeroPantalla.set(resultado)


def igual(num):
    global resultado
    global operacion
    if operacion == "suma":
        numeroPantalla.set(resultado+float(num))
        resultado = 0
    else:
        numeroPantalla.set(resultado-float(num))
    resultado = 0


# Primera fila botones
boton7 = Button(frame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botondiv = Button(frame, text="/", width=3, command=lambda: div())
botondiv.grid(row=2, column=4)

# Segunda fila botones

boton4 = Button(frame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonmult = Button(frame, text="X", width=3, command=lambda: multi())
botonmult.grid(row=3, column=4)

# Tercera fila botones

boton1 = Button(frame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonrest = Button(frame, text="-", width=3,
                   command=lambda: resta(numeroPantalla.get()))
botonrest.grid(row=4, column=4)

# Cuarta fila botones

boton0 = Button(frame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botoncoma = Button(frame, text=",", width=3,
                   command=lambda: numeroPulsado(","))
botoncoma.grid(row=5, column=2)
botonsuma = Button(frame, text="+", width=3,
                   command=lambda: suma(numeroPantalla.get()))
botonsuma.grid(row=5, column=3)
botonigual = Button(frame, text="=", width=3,
                    command=lambda: igual(numeroPantalla.get()))
botonigual.grid(row=5, column=4)


root.mainloop()
