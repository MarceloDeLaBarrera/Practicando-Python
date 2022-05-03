class Curso():

    # Constructor de la clase:
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"

    def mostrar_datos(self):
        print("Nombre: {}  Creditos: {}  Profesion: {}  Imparticion: {}".format(
            self.nombre, self.creditos, self.profesion, self.__imparticion))
        docenteAsignado = self.__verificar_docente()

    def __verificar_docente(self):
        #print("Verificando si existe docente asignado")
        if self.__imparticion == "Presencial":
            print("Si existe un docente asignado")
        else:
            print("No es necesario asignar docente")

     # Metodo __str__ convierte en string la informacion de un objeto. En java es ToString.
    def __str__(self):
        texto = "Nombre: {}  Creditos: {}"
        return texto.format(self.nombre, self.creditos)


curso1 = Curso("Matematicas", 5, "Ingenieria Civil")
print(curso1.nombre, curso1.profesion, curso1.creditos)
curso1.mostrar_datos()

# Llamada al metodo str. Es decir curso1.__str__... No es necesario escribir el .__str__.
print(curso1)
