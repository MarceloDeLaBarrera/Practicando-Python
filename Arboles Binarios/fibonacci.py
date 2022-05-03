# Implementa la función fib(n) que retorna el n-ésimo número de la serie
# de Fibonacci:
# fib(1) = 1
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2), para todo n > 2.


def fib(n):

    if n > 1:
        return fib(n - 1) + fib(n - 2)

    elif n < 0:
        raise Exception("El numero no puede ser menor que 0")

    else:
        return n


def fib2(n):

    if n > 1:
        return fib(n - 1) + fib(n - 2)

    elif n < 0:
        raise Exception("El numero no puede ser menor que 0")

    else:
        return n


if __name__ == "__main__":
    # Prueba de la función: imprime los primeros 10 números en una línea
    # separados por coma y espacio.
    start = 0
    end = 10
    for num in range(start, end):
        prueba_fib = fib(num)
        if num == end-1:
            print(prueba_fib, end="")
        else:
            print(prueba_fib, end=", ")
