import pickle


class Persona():
    # Constructor
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(
            f"Se ha creado una persona nueva, con el nombre de {self.nombre}")

    # Metodo __str__ convierte en string la informacion de un objeto. Sin el, el valor de P que retornaria a "agregarPersonas" seria el valor de los objetos mas no el string que se les asigna.
    def __str__(self):
        return "{} - {} - {}".format(self.nombre, self.genero, self.edad)


class listaPersonas():
    personas = []

    def __init__(self):
        # El constructor solo tiene como parametro listadepersonas que abrirá y agregará "a" al archivo en forma binaria "b", incluyendo lectura "+"

        ficherolista = open(
            "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\guardarinfoficheroexterno", "ab+")
        # seek movera el cursor al inicio del archivo para la lectura, puesto que append hace que quede el cursor al final del archivo.
        ficherolista.seek(0)
        try:
            # Se le asigna a la lista el valor de lo que sea cargado en binario desde el fichero, si no esta creado el fichero, pues lo crea.
            self.personas = pickle.load(ficherolista)
            print(f"Se han cargado {len(self.personas)} personas")
        except:
            print("El fichero esta vacio")

        finally:
            ficherolista.close()

    # METODOS

    # agregarPersonas recibe como parametro un objeto persona, el cual se agregara a la lista personas por medio de append.
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasenFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasenFicheroExterno(self):
        ficherolista = open(
            "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\guardarinfoficheroexterno", "wb")
        pickle.dump(self.personas, ficherolista)
        ficherolista.close()


lista = listaPersonas()
p = Persona("Sandra", "Femenino", 29)
lista.agregarPersonas(p)
p = Persona("Antonio", "Masculino", 15)
lista.agregarPersonas(p)
p = Persona("Jose", "Masculino", 39)
lista.agregarPersonas(p)
p = Persona("Noelia", "Femenino", 12)
lista.agregarPersonas(p)
p = Persona("Camila", "Femenino", 35)
lista.agregarPersonas(p)
lista.mostrarPersonas()
# lista.guardarPersonasenFicheroExterno()
lista = listaPersonas()
lista.mostrarPersonas()
