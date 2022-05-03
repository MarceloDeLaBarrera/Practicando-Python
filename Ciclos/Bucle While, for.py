""" 
Repetir un bucle mientras que usuario digite un numero que cumpla condicion.
numero = int(input("Digite un numero: "))
while numero <= 0:
    numero = int(input("Digite un numero: "))

"""


# Imprimir numeros del 1 al 10.
i = 0
while i < 10:
    print(i+1)
    i += 1   # i=i+1   o el clasico i++ que no se admite en python.

i = 0
while True:
    if i < 10:
        print(i+1)
    else:
        break
    i += 1

# Sintaxis bucle for.. Se hace sobre una coleccion, ya sea lista, tupla, diccionario, etc. Pero tambien puede ser dentro de un rango, para ver cuantas vueltas dara el ciclo.
lista = [100, 200, 300, 400, 500]
nombre = "Marcelo"

for i in lista:
    print(i)

for i in range(0, 5):
    print("hola mundo")

for i in nombre:
    # end hace que el salto de linea de cada iteración del bucle, sea remplazado por lo que se coloque dentro.
    print(i, end=" ")

for i in range(0, 5):
    print("hola mundo")
    if i == 3:
        break

# Simular el  i+4, u otro en ciclo for... Se añade una ultima coma que indica de cuanto en cuanto se hara el salto.
for i in range(0, 17, 4):
    print(i)


# CONTINUE: dentro del if hace que si se cumple la condicion, el ciclo no termina la instruccion y pasa a la siguiente. En este caso, se salta la "e" y "l" e imprime "Marco"
for i in nombre:

    if i == "e" or i == "l":
        continue

    print(i, end=" ")

print("\n")

i = 0
print("Tabla del 5\n")
for x in range(1, 13):
    x *= 5
    i += 1
    print(f"{i} * 5 = {x}")

# Tabla de num y hasta que numero quiere que se multiple (limite), dados por usuario.
num = 5
lim = 12
for x in range(1, lim+1):
    print(f"{x} * {num} = {x*num}")

# Generando tabla de multiplicar del 1 al 10, hasta 10.
for i in range(1, 11):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")


# For anidado
palabras = ["mama", "perro", "juan"]

for palabra in palabras:
    for letras in palabra:
        print(letras, end=" ")
    print(" ")

# for anidado mezclado
numero = [1, 2, 3, 4, 5]
letra = ["a", "b", "c"]

for n in numero:
    for l in letra:  # en vez de letra tambien podria ser un string tipo for l in "abc":
        print(n, l)


list1 = [1, 2, 3, 4, 5]
listx = [5, 4, 3, 2, 1]

for i in range(len(list1)):
    print(list1[0:i])
for i in range(5):
    print(list1[i:5])

for i in range(len(listx)):
    print(listx[i:5])

# Cuenta atras desde un numero dado hasta 0.
numero = 5
for i in range(numero+1):
    print(numero)
    numero -= 1

for i in range(5, -1, -1):
    print(i)

i = 5
while i >= 0:
    print(i)
    i -= 1

# Multiplicando la imprension de un string.
for i in range(6):
    print("*"*(i+1))

# Rellenar lista con datos de una tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
list = []
for i in tupla:
    if i < 5:
        list.append(i)
print(list)


# Range con saltos.
for i in range(0, 21, 4):
    print(i)
