def sumar(a, b):
    return a+b


def restar(a, b):
    return a-b


def multiplicar(a, b):
    return a*b


def elevar(a, b):
    return a**b


def dividir(a, b):

    try:
        return a/b
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
        return "Operacion Erronea"


def redondear(a):
    return round(a)


multiplicar(4, 3)
