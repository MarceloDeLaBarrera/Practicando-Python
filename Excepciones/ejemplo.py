# Ejemplo:

def suma(num1, num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2


def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):
    # Intenta/try dividir, si no se consigue, ejecuta lo que esta dentro del except.
    try:
        return num1/num2

    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
        return "Operacion Erronea"


while True:
    # Bucle infinito, pero, mientras se cumpla lo del try, se hace un break y sale del bucle, si no, se va a la excepcion, imprime su contenido, y luego vuelve al try nuevamente hasta que sean ingresados los valores correctos.

    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))
        break

    except ValueError:
        print("Error, digite un numero, no letras ni caracteres por favor.")

operacion = input(
    "Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
