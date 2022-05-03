# Almacenar sueldos de 4 empleados.
"""
sueldos = []
for i in range(1, 5):
    cash = input(f"Ingrese el sueldo del empleado {i} ")
    sueldos.append(cash)
print(sueldos)

"""
# Hacer que llene una lista inicialmente con el nombre, y luego con las notas.

listax = []
suma = 0
nombre = (input("Ingrese su nombre: "))
count = int(input("Ingrese cantidad de notas: "))


for i in range(count):
    nota = float(input(f"Ingrese la nota {i+1} : "))
    listax.append(nota)
    suma = suma + nota

promedio = suma/count
listax.insert(0, nombre)
print(f"El alumno {listax[0]} , tuvo un promedio de {promedio}")
