# Sintaxis basica

print("hola mundo")

# Declarando variable

mi_nombre = "Mi nombre es Juan"
print(mi_nombre)
print(mi_nombre[3])

# Bucle + identación.
# Se imprime a por cada vuelta del bucle, es decir, esta dentro del bucle el print
a = 0
for i in range(5):
    a = a+1
    print(a)

# Se imprime el valor de "a" al finalizar el bucle, puesto que se encuentra fuera de el.
a = 0
for i in range(5):
    a += 1
print(a)

# OPERADORES

# suma
a = 5+6
print(a)

# Resto
a = 10 % 3
print(a)

# Exponencial
a = 5**3
print(a)

# Division
a = 9/2
print(a)

# Tipo de dato Boleano
b = True
c = False
print(type(b), type(c))

# En python la variable viene definida por el contenido, por eso no es necesario declarar el tipo de la variable previamente
# Python es un lenguaje 100% orientado a objetos, al declarar una variable, para python es un objeto.

# Funcion Type: Señala que variable nombre es objeto que pertenece a la clase String
nombre = "Juan perez"
print(type(nombre))

# Saltos de linea dentro de un texto, se hace con 3 comillas.
mensaje = """Esto es un mensaje
con tres
saltos de linea"""
print(mensaje)

# Condicional + Concadenación ... ":" al final de la primera linea de un bucle o condicional indica que el codigo continua en la linea de abajo. "," se usa para concadenar.
numero1 = 8
numero2 = 5

if numero2 > numero1:
    print(numero2, " Es mayor que ", numero1)

elif numero2 == numero1:
    print("Ambos numeros son iguales")

else:
    print(f"{numero2} es menor que {numero1}")
