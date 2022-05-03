import mysql.connector
from mysql.connector import Error

# Data Access Object


class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="sasasa",
                db="universidad"
            )

        except Error as Ex:
            print("Error al intentar conexion {}".format(Ex))

    def mostrarCursos(self):
        """Si la conexion se ha establecido, se crea cursor que permite realizar querys y luego se ejecuta. 
        Luego con fetchall se extran todos los registros en forma de tuplas dentro de una lista, almacenando dicha lista a una variable, y retornandola"""

        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = "SELECT * FROM cursos ORDER BY nombre ASC "
                cursor.execute(query)

                resultado = cursor.fetchall()
                return resultado

            except Error as Ex:
                print("Error al intentar conexion {}".format(Ex))

    def crearCursos(self, cursos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = "INSERT INTO cursos VALUES (%s,%s,%s)"
                cursor.execute(query, (cursos[0], cursos[1], cursos[2]))
                self.conexion.commit()
                print("Curso registrado exitosamente\n")

            except Error as Ex:
                print("Error al intentar conexion {}".format(Ex))

    def actualizarCurso(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = "UPDATE cursos SET nombre=%s, creditos=%s WHERE codigo=%s"
                cursor.execute(query, (codigo[0], codigo[1], codigo[2]))
                self.conexion.commit()
                print("Curso actualizado exitosamente\n")

            except Error as Ex:
                print(
                    "Error al intentar conexion {}".format(Ex))

    def eliminarCurso(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = "DELETE FROM cursos WHERE codigo=%s"
                cursor.execute(query, (codigo,))
                self.conexion.commit()
                print("Curso eliminado exitosamente\n")

            except Error as Ex:
                print(
                    "Error al intentar conexion {}".format(Ex))


help(DAO.mostrarCursos)
