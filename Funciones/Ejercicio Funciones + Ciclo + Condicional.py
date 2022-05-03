"""Ejercicio 5: 
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones: 
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir"""


saldo = 0
opcion = 0
monto = 0


def opcion1():
    global saldo
    if opcion == 1:
        while True:
            monto = int(input("Ingrese monto: "))
            if monto > 0:
                break
            else:
                print("ERROR: Ingrese una cantidad valida")

        saldo = saldo + monto
        print("Monto ingresado satisfactoriamente")
        print(f"Su saldo disponible es: {saldo}")


def opcion2():
    global saldo
    global monto

    if opcion == 2:
        while True:
            monto = int(input("Ingrese monto a retirar: "))
            if monto > 0:
                break
            else:
                print("ERROR: Ingrese una cantidad valida de retiro")

        if saldo == 0:
            print("No posee saldo suficiente")

        elif saldo < monto:
            print("No posee suficiente saldo para hacer el retiro")
            print(f"Su saldo disponible es: {saldo}")

        else:
            saldo = saldo - monto
            print("Retiro Exitoso")
            print(f"Su saldo disponible es: {saldo}")


def opcion3():
    global saldo
    if opcion == 3:
        print(f"Su saldo disponible es: {saldo}")


def opcion4():
    if opcion == 4:
        print("Que tenga un buen dia")


def MENU():
    global saldo
    global opcion
    menu = """  MENU
    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir"""
    print(menu)
    opcion = int(input("Seleccione una opcion: "))
    opcion1()
    opcion2()
    opcion3()
    opcion4()
    if opcion == 1 or opcion == 2 or opcion == 3:
        MENU()
    else:
        return(0)


"""
while True:
    MENU()
    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
        break
    else:
        print("ERROR, SELECCIONE UNA OPCION VALIDA")

"""


for opcion in range(999999):
    MENU()
    if opcion <= 0 or opcion > 4:
        print("ERROR, SELECCIONE UNA OPCION VALIDA")
    elif opcion == 4:
        break
