# Las funciones decoradoras, son funciones que añaden funcionalidades a otras funciones.


# *args -->Indica a una funcion que puede recibir un numero indeterminado de parametros
# *kwargs-->Indica a una funcion que puede recibir parametros del tipo clave valor.
def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        print("Realizando calculo...")
        funcion_parametro(*args, **kwargs)
        print("Calculo Realizado")

    return funcion_interna


# Anteponer el "@" junto con el nombre de la funcion decoradora, permite indicarle a la funcion suma que tiene mas funcionalidades que provienen de la funcion decoradora.

@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)


@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(7, 2)
potencia(base=5, exponente=2)
