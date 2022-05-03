import time


# Esta es mas eficiente.
def suma_constante(n):
    return (n/2)*(n+1)


def suma_lineal(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


t0 = time.time()
suma1 = suma_constante(100000000)
t1 = time.time()
suma2 = suma_lineal(100000000)
t2 = time.time()


# A medida que mas crece el numero, mas tiempo le toma a la forma tradicional.
print(f"{suma1}\n{t1-t0}")
print(f"{suma2}\n{t2-t1}")
