import json
from json.encoder import JSONEncoder
import os
import pathlib


class Libro():
    def __init__(self, isbn, tit, aut):
        self._isbn = isbn
        self._titulo = tit
        self._autor = aut

    # Metodos get y set....

    # Metodo str, el que permite mostrar un objeto libro al printearlo.
    def __str__(self):
        return f"ISBN: {self._isbn}\nTitulo: {self._titulo}\nAutor: {self._autor}"


# Json Encoder funcion default, toma como parametro un objeto, y, si el objeto es instancia de la clase, devuelve un diccionario, que contiene la clave y el valor del objeto.atributo y que será almacenado en el archivo JSON.
class libroEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Libro):
            return {"ISBN": obj._isbn, "Titulo": obj._titulo, "Autor": obj._autor}
        else:
            # La clase jsonEncoder se encarga de devolver el error correspondiente.
            return json.JSONEncoder.default(self, obj)


# Recibe diccionario para generar un objeto libro
def from_json(dict):
    return Libro(dict["ISBN"], dict["Titulo"], dict["Autor"])


class Biblioteca():
    agregar_libro = 1
    consultar_libro = 2
    salir = 0

    def __init__(self):
        self._libros = []
        self.recuperar_libros("libros.json")

    # Metodo destructor
    def __del__(self):
        self.almacenar_libros("libros.json")

    # Metodos get y set
    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self, lib):
        self._libros = lib

    # Metodos

    # Revisa archivo json de BBDD, y carga la información en variable data, luego se recorre el diccionario y se almacena convertido en objeto dentro de la lista "libros"
    def recuperar_libros(self, ruta):
        # Si existe la ruta, abrir el archivo en modo lectura y cargarlo.
        if pathlib.Path(ruta).exists():
            with open(ruta, "r") as file:
                data = json.load(file)

            for lib in data["Libros"]:
                self.libros.append(from_json(lib))

    # Almacena los objetos libro que haya en la lista de libros dentro del archivo BBDD json, indicando que debera usar libroEncoder para convertir los objetos en diccionario, cls=class
    def almacenar_libros(self, ruta):
        with open(ruta, "w") as file:
            json.dump({"Libros": self.libros}, file,
                      indent=2, cls=libroEncoder)

    def agregar_libros(self):
        os.system("cls")
        print("Agregar Libro:")
        isbn = input("ISBN: ")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        lib = Libro(isbn, titulo, autor)
        self.libros.append(lib)

    def consultar_libros(self):
        os.system("cls")
        print("Libros: \n")
        if len(self.libros) == 0:
            print("\nNo hay libros en la biblioteca")
        else:
            for lib in self.libros:
                print(lib)
                print("-"*40)

    def menu(self):
        continuar = True
        while continuar:
            os.system("cls")
            print(
                f"Biblioteca\n{Biblioteca.agregar_libro})Agregar Libro\n{Biblioteca.consultar_libro})Consultar Libro\n{Biblioteca.salir})Salir")
            opc = int(input("Seleccione una opcion: "))

            if opc == Biblioteca.agregar_libro:
                self.agregar_libros()
            elif opc == Biblioteca.consultar_libro:
                self.consultar_libros()
            elif opc == Biblioteca.salir:
                os.system("cls")
                continuar = False
            else:
                os.system("cls")
                print("\nOpcion no valida")

            input("Presione enter para continuar")


def main():
    bib = Biblioteca()
    bib.menu()


if __name__ == "__main__":
    main()
