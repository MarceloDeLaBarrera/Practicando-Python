# La funcion Filter verifica que los elementos de una secuencia (como una lista por ej), cumplan una condicion, devolviendo un iterador con los elementos que cumplen la condicion.
#  es del tipo orden superior, y permite usar paradigma de programacion funcional.

def numeropar(num):
    if num % 2 == 0:
        return True
    else:
        return False


lista1 = [20, 12, 32, 43, 43, 65, 54, 76, 87, 56, 34, 67, 34, 56, 77, 55]

print(list(filter(numeropar, lista1)))

print(list(filter(lambda num: num % 2 == 0, lista1)))


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


salarios_altos = filter(lambda sal: sal.money > 50000, listaEmpleados)

for salarios in salarios_altos:
    print(salarios)


# Sin lambda ni filter podria ser:
def salarioalto(lista):
    for empleado in lista:
        if empleado.money > 50000:
            print(empleado)


salarioalto(listaEmpleados)
