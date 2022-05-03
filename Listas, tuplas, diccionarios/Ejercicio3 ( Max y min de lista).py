# Calcular el valor minimo y maximo de una lista

Lista1 = [3, 4, 5, 6, 7, 4, 2, 2, 1, 5, 6, 7, 8, 555, 2, 2, 4]
pos = Lista1.index(min(Lista1))
print(min(Lista1), pos)
print(max(Lista1))


def Menor(numeros):

    minimo = numeros[0]
    for i in numeros:
        if i < minimo:
            minimo = i
    return minimo


def Mayor(numeros):

    maximo = numeros[0]
    for i in numeros:
        if i > maximo:
            maximo = i
    return maximo


print(Menor(Lista1))
print(Mayor(Lista1))


k = 0
posicion = 0
canti = Lista1[0]
while k < len(Lista1):
    if Lista1[k] < canti:
        canti = Lista1[k]
        posicion = k

    k += 1
print(f"El valor es: {canti} y se encuentra en la posicion {posicion+1}")

k = 0
canti = Lista1[0]
while k < len(Lista1):
    if Lista1[k] > canti:
        canti = Lista1[k]
    k += 1
print(canti)
