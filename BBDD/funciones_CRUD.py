def mostrarcursos(cursos):
    """Recibe como parametro una lista "cursos", que contiene tuplas de cada registro. Y se accede a la posicion 0,1 y 2 de cada registro. """

    print("\nCursos: \n")
    for tupla in cursos:
        print(
            f"Codigo: {tupla[0]} | Nombre: {tupla[1]}  ({tupla[2]} Creditos)")


def inputCursos():
    """Solicita codigo, nombre y creditos, y almacena éstos dentro de una lista, la cual es retornada por la funcion"""

    creditoscorrecto = False

    while True:
        codigo = input("Ingrese Codigo del curso: ")
        if len(codigo) == 6:
            break
        else:
            print("Error, ingrese un codigo de 6 digitos")

    nombre = input("Ingrese Nombre del curso: ")

    while not creditoscorrecto:
        creditos = input("Ingrese creditos del curso: ")
        if creditos.isnumeric():
            if int(creditos) > 0:
                creditoscorrecto = True
            else:
                print("Error, los creditos deben ser mayor que 0")
        else:
            creditoscorrecto = False
            print("Error, por favor ingrese un valor numerico")

    cursos = (codigo, nombre, creditos)
    return cursos


def eliminarCurso(cursos):
    """Recibe como parametro una lista "cursos", y se solicita que ingrese un codigo. Luego se recorre la lista y se compara si la tupla en posicion 0 que corresponde al codigo es igual al codigo solicitado.
    Si es igual, corta el ciclo, y retorna el codigo, si no, retorna como vacio el codigo"""

    codigoExiste = False
    codigo = input("Ingrese Codigo del curso que desea eliminar: ")
    for cur in cursos:
        if cur[0] == codigo:
            codigoExiste = True
            break

    if not codigoExiste:
        codigo = ""

    return codigo


def actualizarCurso(cursos):
    """Se le pasa como parametro una lista curso. Luego solicita codigo de un curso, y se recorre la lista comparando en la posicion 0 si ambos valores son iguales. Si lo son, 
    se solicita que se ingresen los datos a modificar en nombre y creditos y remplaza y asigna esos valores a la lista cursos, si no, remplaza el valor de cursos por un None. Finalmente retorna "cursos"""

    creditoscorrecto = False
    codigoExiste = False

    codigo = input("Ingrese Codigo del curso que desea actualizar: ")
    for cur in cursos:
        if cur[0] == codigo:
            codigoExiste = True
            break

    if codigoExiste:

        nombre = input("Ingrese nuevo nombre para el curso: ")

        while not creditoscorrecto:
            creditos = input(
                "Ingrese los nuevos creditos que tendrá el curso: ")
            if creditos.isnumeric():
                if int(creditos) > 0:
                    creditoscorrecto = True
                else:
                    print("Error, los creditos deben ser mayor que 0")
            else:
                creditoscorrecto = False
                print("Error, por favor ingrese un valor numerico")

        cursos = (nombre, creditos, codigo)
    else:
        cursos = None

    return cursos


# Para ver documentación, se utiliza  help o __doc__ y se le pasa como parametro la funcion de la que se desea ver la documentacion... Para documentar se usa triple comilla.
help(actualizarCurso)
print(f"Funcion Eliminar Cursos: {eliminarCurso.__doc__}")
