from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

root = Tk()
frame = Frame()
frame.pack()
root.title("Menu")

# VENTANAS EMERGENTES


def infoAdicional():
    messagebox.showinfo("Procesador de Marcelo", "Procesador de textos 2021")


def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto sin licencia")


def salirSioNo():
    # askquestion= "yes"or "not". (Si no)
    # askokcancel= True or False. ( aceptar cancelar)
    #value = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
    value = messagebox.askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if value == True:
        root.destroy()


def abreFichero():
    fichero = filedialog.Open()
    show = fichero.show()
    os.chdir("C:\\")

    print(fichero)


# CREANDO MENU, se crea objeto MENU, cuyo parametro es la raiz. En el root.config se le esta configurando el menu a la raiz.
barramenu = Menu(root)
root.config(menu=barramenu)
root.geometry("720x480")


# tearoff elimina la linea separadora debajo de cada seccion de menu

# Se crea objeto archivo menu, llamando a la clase Menu y pasandole como parametro el objeto menu llamado barramenu que creamos anteriormente.
archivoMenu = Menu(barramenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirSioNo)


edicionMenu = Menu(barramenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_command(label="Cortar")


herramientasMenu = Menu(barramenu)

ayudaMenu = Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)

# add_cascade permite indicar que los elementos creados anteriormente pertenecen a "x" seccion del menu.
barramenu.add_cascade(label="Archivo", menu=archivoMenu)
barramenu.add_cascade(label="Edicion", menu=edicionMenu)
barramenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()
