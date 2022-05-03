# Muchas-formas... Un objeto puede cambiar de forma dependiendo del contexto en que se utilice, por lo que tambien cambiarian sus metodos.

class Coche():

    def __init__(self):
        pass

    def desplazamiento(self):
        print("Desplazamiento en 4 ruedas")


class Moto():

    def __init__(self):
        pass

    def desplazamiento(self):
        print("Desplazamiento en 2 ruedas")


class Camion():

    def __init__(self):
        pass

    def desplazamiento(self):
        print("Desplazamiento en 6 ruedas")


# Funcion que recibe como parametro un objeto de una clase, invocando al metodo desplazamiento de la susodicha.
# Como todas las clases planteadas tienen mismo nombre de metodo, invocara al metodo de dicha clase.
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()


vehiculo1 = Moto()
vehiculo1.desplazamiento()

desplazamientovehiculo(vehiculo1)

vehiculo2 = Coche()
vehiculo2.desplazamiento()

# Vehiculo 3 es una lista con 3 objetos de diferentes clases.
vehiculo3 = [Coche(), Moto(), Camion()]
for v in vehiculo3:
    desplazamientovehiculo(v)
