# Sintaxis
# Se utiliza la expresion yield en medio, es similar a una funcion, pero es mas eficiente.

# Ejemplo: Funcion o generador que retorne los primeros numeros pares dado un limite "x".

# Funcion
def generarPares(limite):
    num = 1
    lista = []

    while num < limite:
        lista.append(num*2)
        num += 1

    return lista


print(generarPares(10))

# Generador no retorna nada.


def generadorPares(limite):
    num = 1

    while num < limite:
        # Con Yield se convierte en generador, que permite crear un objeto iterable que genera los valores de uno en uno, sin necesidad de almacernarlos en una lista.
        yield num*2   # yield= generar
        num += 1


# almacenadorpar es un variable objeto iterable que almacena al generador.
almacenadorpar = generadorPares(10)

for i in almacenadorpar:
    print(i, end=" ")

print("\n")


# El arterisco antes del parametro, indica que puede ser 1 o mas elementos que recibira y que vendran en forma de tupla.
def devuelveCiudad(*ciudades):
    for element in ciudades:
        """for letras in element: #ciclo for anidado, para recorrer las letras del elemento
            yield letras"""
        yield from element  # Generar "desde" el primer elemento


ciudadesDevueltas = devuelveCiudad(
    "Santiago", "Valparaiso", "Iquique", "Ovalle", "Coquimbo")

for i in ciudadesDevueltas:
    print(i, end=" ")
