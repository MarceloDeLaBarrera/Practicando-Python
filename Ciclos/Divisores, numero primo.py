# Factores/Divisores de 3 dentro de una lista.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
Divisor3 = []
Primes1 = []
Primes2 = []
Primes3 = []

for number in list:
    if number % 3 == 0:
        Divisor3.append(number)
print(Divisor3)


# Funcion Booleana. Determina True o False si numero es primo.
# Si numero es menor o igual a 1, entonces no es primo, porque parten del 2 en adelante.
# Dentro del ciclo i se movera en el rango entre 2 y el valor del numero ingresado.
# Si se cumple que al dividir el numero ingresado entre el rango establecido de "i", y se obtiene resto 0, considerando que "i" sea distinto del numero ingresado, retorna False, es decir, no es primo.
# Si no se cumple lo anterior, es decir, numero ingresado al dividirse por si mismo da igual 0, entonces es True y es verdadero.

def prime(num):

    if num <= 1:
        return False

    for i in range(2, num+1):
        if num % i == 0 and i != num:
            return False

    return True


for number in list:
    if prime(number):  # if prime(number) == True:
        Primes1.append(number)

print(Primes1)


# -------------------------------------------------------------------------------------------------------------------------------------------------------


# Tambien puede ser en un rango tipo: for i in range(1,100)
for number in list:
    count = 0

    for j in range(1, number+1):
        if number % j == 0:
            count += 1

    if count <= 2 and number > 1:
        Primes2.append(number)

print(Primes2)


def primos(num):

    for i in range(1, num+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1

        if count == 2 and i > 1:
            print(i)


primos(100)


def primos(n):
    """
    Función que recibe un numero "n" y retorna los primeros "n" numeros primos.
    """
    # Para i en un rango entre 1 y n+1, ya que range no considera el ultimo valor.
    for i in range(1, n+1):
        # Se establece variable divisor en 0, para poder contar la cantidad de divisores de cada numero i.
        divisor = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor += 1
            # Si J es divisor de i, añade uno a variable divisor. Se comparan todos los J dentro del rango del valor de i.
            # Ademas, cuando terminan de iterarse los valores de j en i, y empieza una nueva iteración de i, la variable divisor vuelve a tomar el valor de 0.
            # Ej: Para 7, se comparan todos los numeros del 1 al 7. Si 7 es divisible solo por 1 y por si mismo, seria primo.

        if divisor == 2 and i > 1:
            # Se printea el numero i que cumpla la condicion de tener dos divisores y ser mayor que 1, que es la condicion para que un numero sea primo (divisible por 1 y por si mismo).
            print(i)


primos(100)
