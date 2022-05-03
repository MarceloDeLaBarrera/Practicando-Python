
class Persona():

    def __init__(self, nom, eda):
        self._nombre = nom
        self._edad = eda

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nom):
        self._nombre = nom

    def getEdad(self):
        return self._edad

    def getEdad(self, eda):
        self._edad = eda

    def __str__(self):
        return f"Nombre: {self.nombre} | Edad: {self._edad}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, prom, cod):
        super().__init__(nombre, edad)
        self._promedio = prom
        self._codigo = cod

    def estudiar(self, materia):
        print(f"{self.nombre} esta estudiando {materia}")

    def __str__(self):
        return f"{super().__str__()} | Promedio: {self._promedio} | Codigo: {self._codigo}"


Pers1 = Persona("Marcelo", 15)
print(Pers1)
est = Estudiante("Juan", 15, 6.5, 1273782)
print(est)
