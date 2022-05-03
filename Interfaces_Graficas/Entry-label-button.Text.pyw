from tkinter import *

root = Tk()
frame = Frame(root, width=1280, height=720)
frame.pack()

# Clase entry permite crear el cuadro de texto donde el usuario podra ingresar valores. Lo que aplica para labels tambien aplica para Entry.
# Widget Text permite crear cuadros de texto extensos, cuadros de comentarios, donde usuario se explaya. Button = Botones.
# grid construye una tabla con filas y columnas determinadas.
# sticky permite alinear segun punto cardinalidad (norte, sur, este, oeste)
# Pady y Padx establece los limites entre contenedor y lo que se contiene.

# Stringvar permite capturar el string ingresado dentro del campo Entry
minombre = StringVar()

cuadrotexto = Entry(frame, textvariable=minombre)
cuadrotexto.grid(row=0, column=1, padx=5, pady=5)
cuadrotexto.config(justify="center")
label1 = Label(frame, text="Nombre: ", padx=5, pady=5)
label1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

cuadrotexto2 = Entry(frame)
cuadrotexto2.grid(row=1, column=1, padx=5, pady=5)
cuadrotexto2.config(justify="center")
label2 = Label(frame, text="Apellido: ", padx=5, pady=5)
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

cuadrotexto3 = Entry(frame)
cuadrotexto3.grid(row=2, column=1, padx=5, pady=5)
cuadrotexto3.config(justify="center")
label3 = Label(frame, text="Direccion: ", padx=5, pady=5)
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)

cuadrotexto4 = Entry(frame)
cuadrotexto4.grid(row=3, column=1, padx=5, pady=5)
cuadrotexto4.config(justify="center", show="*")
label4 = Label(frame, text="Contraseña: ", padx=5, pady=5)
label4.grid(row=3, column=0, sticky="w", padx=5, pady=5)

Cuadrogrande = Text(frame, width=50, height=10)
Cuadrogrande.grid(row=4, column=1, padx=5, pady=5)
# Scrollbar dentro de frame, asociada a Text que esta en el eje y "yview"
SB = Scrollbar(frame, command=Cuadrogrande.yview)
SB.grid(row=4, column=2, sticky="nse")
Cuadrogrande.config(yscrollcommand=SB.set)

label5 = Label(frame, text="Comentarios: ", padx=5, pady=5)
label5.grid(row=4, column=0, sticky="w", padx=5, pady=5)


def codigoboton():
    minombre.set("Marcelo")


autorellenarboton = Button(root, text="Enviar", command=codigoboton)
autorellenarboton.pack()

root.mainloop()
