# Ejemplo
#input= array[5,4,3,6,5,4,2,6,7,8]
#output= (54)-3654-2678

lista = [5, 4, 3, 6, 5, 4, 2, 6, 7, 8]
lista = "".join(str(lista).split(", "))
lista = f"({lista[1:3]})-{lista[3:7]}-{lista[7:]}"
print(lista.strip("]"))


lista = [5, 4, 3, 6, 5, 4, 2, 6, 7, 8]


def listado(n):

    lista = "".join(str(i) for i in n)
    lista = f"({lista[0:2]})-{lista[2:6]}-{lista[6:]}"
    return lista


def listado2(n):
    return "({}{})-{}{}{}{}-{}{}{}{}".format(*n)


print(listado(lista))
print(listado2(lista))
