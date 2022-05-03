lista = [4, 5, 4, 66, 7, 8, 5, 22, 1]

k = 0
value = int(input("What number are you looking for?: "))
# Aca "i" toma el valor del primer,segundo, y asi sucesivamente element de la lista para iterar y compara si el valor ingresado es igual al valor de la lista.
for i in lista:
    if value == i:
        print(f"The number it's on position {k+1}")
        break

    k += 1

if value != i:
    print("Not found")


k = 0
value = int(input("What number are you looking for?: "))
# Aca "i" toma el valor del largo de la lista para iterar y compara el valor de la lista en posicion i con valor ingresado.
for i in range(len(lista)):
    if lista[i] == value:
        print(i+1)
        break

if value != lista[i]:
    print("Not found")
