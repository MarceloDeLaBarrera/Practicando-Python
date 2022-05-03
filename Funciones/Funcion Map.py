# La funcion map sirve para aplicar una funcion a cada uno de los objetos dentro de una lista.

class Empleado():
    def __init__(self, nombre, cargo, salario):
        self.name = nombre
        self.job = cargo
        self.money = salario

    def __str__(self):
        return f"{self.name} que trabaja como {self.job} y tiene un salario de ${self.money}"


listaEmpleados = [
    Empleado("Jorge", "Director", 75000), Empleado("Juan", "Obrero", 50000),
    Empleado("Marcelo", "Informatico", 20000), Empleado(
        "Pedro", "Analista", 60000),
    Empleado("Samuel", "Constructor", 85000)
]


def calculocomision(lista):
    if lista.money <= 50000:
        lista.money = lista.money*1.03
    return lista


listaempleados2 = map(calculocomision, listaEmpleados)
for empleado in listaempleados2:
    print(empleado)

listaEmpleadosComision = map(lambda empleado: empleado.money * 1.03,
                             filter(lambda empleado: empleado.money <= 500000, listaEmpleados))


def elevarcuadrado(num):
    return num**2


nums = list(range(1, 11))
numeroselevados = list(map(elevarcuadrado, nums))
print(numeroselevados)
