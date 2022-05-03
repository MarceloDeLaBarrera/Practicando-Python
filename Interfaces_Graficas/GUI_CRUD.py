from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
from mysql.connector import cursor

root = Tk()
frame = Frame(root)
frame.pack()
frame2 = Frame(root)
frame2.pack()
root.title("CRUD")


connect = mysql.connector.connect(
    host="localhost",
    username="root",
    password="sasasa",
    db="crudgui")

# VENTANAS EMERGENTES


def conexion():
    try:
        cursor = connect.cursor(buffered=True)
        query = """CREATE TABLE IF NOT EXISTS usuarios (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50),
                password VARCHAR(50) NOT NULL,
                direccion VARCHAR(50),
                comentarios VARCHAR(100),
                PRIMARY KEY (id)
                )  """

        cursor.execute(query)
        messagebox.showinfo("BBDD", "Conexión exitosa.")

    except:
        messagebox.showwarning(
            "¡Atención!", "No se pudo establecer la conexión")


def salirSioNo():
    # askokcancel= True or False. ( aceptar cancelar)

    connect.close
    value = messagebox.askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if value == True:
        root.destroy()


def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto sin licencia")


def limpiarcampos():
    id.set("")
    nombre.set("")
    apellido.set("")
    password.set("")
    direccion.set("")
    campoComentarios.delete(1.0, END)


def crear():
    query = "INSERT INTO usuarios (nombre, apellido, password, direccion, comentarios) VALUES (%s,%s,%s,%s,%s)"
    cursor = connect.cursor(buffered=True)

    cursor.execute(query, (nombre.get(), apellido.get(), password.get(
    ), direccion.get(), campoComentarios.get(1.0, END)))

    connect.commit()
    messagebox.showinfo("BBDD", "Registro insertado correctamente")


def leer():
    query = "SELECT * FROM usuarios WHERE id=%s"
    cursor = connect.cursor(buffered=True)
    cursor.execute(query, (id.get(),))

    usuario = cursor.fetchall()
    for u in usuario:
        id.set(u[0])
        nombre.set(u[1])
        apellido.set(u[2])
        password.set(u[3])
        direccion.set(u[4])
        campoComentarios.insert(1.0, u[5])

    connect.commit()
    messagebox.showinfo("BBDD", "Lectura Exitosa")


def actualizar():
    query = "UPDATE usuarios SET nombre=%s, apellido=%s, password=%s, direccion=%s, comentarios=%s WHERE id=%s "
    cursor = connect.cursor(buffered=True)

    cursor.execute(query, (nombre.get(), apellido.get(), password.get(
    ), direccion.get(), campoComentarios.get(1.0, END), id.get()))

    connect.commit()
    messagebox.showinfo("BBDD", "Actualizacion exitosa del registro")


def eliminar():
    query = "DELETE FROM usuarios WHERE id=%s"
    cursor = connect.cursor(buffered=True)
    cursor.execute(query, (id.get(),))

    connect.commit()
    messagebox.showinfo("BBDD", "Registro borrado exitosamente")


# CREACION DEL MENU
barramenu = Menu(root)
root.config(menu=barramenu)
root.geometry("300x450")

bbddMenu = Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexion)
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salirSioNo)


borrarMenu = Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarcampos)

crudMenu = Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Eliminar", command=eliminar)


ayudaMenu = Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...")

barramenu.add_cascade(label="BBDD", menu=bbddMenu)
barramenu.add_cascade(label="Borrar", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# Creacion de campos y labels.

id = StringVar()
nombre = StringVar()
apellido = StringVar()
password = StringVar()
direccion = StringVar()

campoID = Entry(frame, textvariable=id)
campoID.grid(row=0, column=1, padx=5, pady=5)
campoID.config(justify="center")
labelID = Label(frame, text="ID: ", padx=5, pady=5)
labelID.grid(row=0, column=0, sticky="e", padx=5, pady=5)

campoNombre = Entry(frame, textvariable=nombre)
campoNombre.grid(row=1, column=1, padx=5, pady=5)
campoNombre.config(justify="center")
labelNombre = Label(frame, text="Nombre: ", padx=5, pady=5)
labelNombre.grid(row=1, column=0, sticky="e", padx=5, pady=5)

campoApellido = Entry(frame, textvariable=apellido)
campoApellido.grid(row=2, column=1, padx=5, pady=5)
campoApellido.config(justify="center")
labelApellido = Label(frame, text="Apellido: ", padx=5, pady=5)
labelApellido.grid(row=2, column=0, sticky="e", padx=5, pady=5)

campoPassword = Entry(frame, textvariable=password)
campoPassword.grid(row=3, column=1, padx=5, pady=5)
campoPassword.config(justify="center", show="*")
labelPassword = Label(frame, text="Password: ", padx=5, pady=5)
labelPassword.grid(row=3, column=0, sticky="e", padx=5, pady=5)

campoDireccion = Entry(frame, textvariable=direccion)
campoDireccion.grid(row=4, column=1, padx=5, pady=5)
campoDireccion.config(justify="center")
labelDireccion = Label(frame, text="Direccion: ", padx=5, pady=5)
labelDireccion.grid(row=4, column=0, sticky="e", padx=5, pady=5)

campoComentarios = Text(frame, width=15, height=10)
campoComentarios.grid(row=5, column=1, padx=5, pady=5)
# Scrollbar dentro de frame, asociada a Text que esta en el eje y "yview"
SB = Scrollbar(frame, command=campoComentarios.yview)
SB.grid(row=5, column=2, sticky="nse")
campoComentarios.config(yscrollcommand=SB.set)

labelComentarios = Label(frame, text="Comentarios: ", padx=5, pady=5)
labelComentarios.grid(row=5, column=0, sticky="e", padx=5, pady=5)


# Creacion de botones

botonCrear = Button(frame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="w", padx=10, pady=10)


botonLeer = Button(frame2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="w", padx=10, pady=10)


botonActualizar = Button(frame2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="w", padx=10, pady=10)


botonBorrar = Button(frame2, text="Delete", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="w", padx=10, pady=10)


root.mainloop()
