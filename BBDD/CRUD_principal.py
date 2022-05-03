from BBDD_CRUD import DAO
import funciones_CRUD as funciones


def menuPrincipal():
    continuar = True
    opcioncorrecta = False

    while continuar:
        while not opcioncorrecta:
            print("===========================Menu Principal===========================")
            print("1.- Mostrar Cursos")
            print("2.- Crear Curso")
            print("3.- Actualizar Curso")
            print("4.- Eliminar Curso")
            print("5.- Salir")
            print("====================================================================")

            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese nuevamente un numero")

            elif opcion == 5:
                continuar = False
                print("Gracias por usar este sistema")
                opcioncorrecta = True

            else:
                ejecutaropcion(opcion)


def ejecutaropcion(o):
    dao = DAO()

    if o == 1:
        try:
            cursos = dao.mostrarCursos()
            if len(cursos) > 0:
                funciones.mostrarcursos(cursos)

            else:
                print("No se encontraron cursos.")
        except:
            print("Ocurrio un error")

    elif o == 2:
        cursos = funciones.inputCursos()
        try:
            dao.crearCursos(cursos)
        except:
            print("Ocurrio un error")

    elif o == 3:
        try:
            cursos = dao.mostrarCursos()
            if len(cursos) > 0:
                funciones.mostrarcursos(cursos)
            codigoActualizar = funciones.actualizarCurso(cursos)
            if not codigoActualizar == None:
                dao.actualizarCurso(codigoActualizar)
            else:
                print("Error, codigo de curso a actualizar no encontrado")

        except:
            print("Ocurrio un error")

    elif o == 4:
        try:
            cursos = dao.mostrarCursos()
            if len(cursos) > 0:
                funciones.mostrarcursos(cursos)
            codigoEliminar = funciones.eliminarCurso(cursos)

            if not codigoEliminar == "":
                dao.eliminarCurso(codigoEliminar)
            else:
                print("Error, el codigo ingresado no se encuentra en la base de datos")

        except:
            print("Ocurrio un error, ingrese un codigo valido")


menuPrincipal()
