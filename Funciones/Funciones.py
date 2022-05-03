# Sintaxis Funciones

# Declaracion de funcion
def nombre_funcion():
    # instrucciones
    valor = 1
    return(valor)  # opcional, no todas las funciones retornan un valor.


nombre_funcion()  # Modo de llamar funsión.


def mensaje():
    print("hola mundo")
    print("hola mundo")
    print("hola mundo")
    print("hola mundo")
    print("hola mundo")


# En este caso al llamar la funcion como contiene prints, se printean.
mensaje()

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# La funcion volumen_cubo llama y retorna a la funcion cubo. En funcion cubo se hace el calculo y en volumen_cubo se retorna el valor del calculo de cubo.


def volumen_cubo(lado):
    return cubo(lado)


def cubo(n):
    valor = n*n*n
    return (valor)

# Parseo para indicar que lo que se captura es un valor entero.


#print("Ingrese uno de los lados del cubo:")
#a = int(input())
a = int(input("Ingrese uno de los lados del cubo: "))
#print("El volumen del cubo es", volumen_cubo(a))
print(f"El volumen del cubo es {volumen_cubo(a)}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def suma(num1, num2):
    a = num1+num2
    print(a)


print("Sumas con funcion suma: ")
suma(1, 2)
suma(10, 15)
suma(10, 20)


def resta(num1, num2):
    resultado = num1-num2
    return(resultado)


print(resta(5, 2))

# ----------------------------------------------------------------------------------------------------------------------------------------------------
