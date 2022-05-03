# Parseo
n = "5"
n = int("5")
print(type(n))
n = str(5)
print(type(n))

# Redondeo
n = round(5.5)
print(n)

# Upper y lower, pasar todo a mayus o minus.
nombre = "MaRcElo"
nombre = nombre.upper()
print(nombre)

# Obtener ultimo elemento de un string:
print(nombre[-1])

# Cuenta letras.
oracion = "Mi mama me mima"
oracion = oracion.lower()
print(oracion.count("m"))


# Reemplazar
mensaje = "Camaron que se duerme, se lo lleva la marea"
mensaje = mensaje.replace("marea", "corriente")
print(mensaje)

# Largo... Ojo Len, empieza a contar de 1 en adelante, no desde 0.
largonombre = nombre.__len__()
print(largonombre)
n = len(nombre)
print(n)

# Capitalize pone la primera letra en mayus y las otras en minus..
print(nombre.capitalize())

# Find representa el indice en que se encuentra un caracter.
Texto = "Mama mama mama"
print(Texto.find("a"))

# isdigit verifica si es un numero o caracter devolviendo True o False.
# isalnum verifica si es alfanumerico o no
# isalpha verifica si son solo letras, sin espacios.
Num = "5"
t = "Chocolate f"
print(Num.isdigit())
print(Num.isalnum())
print(t.isalpha())


# Recorriendo string
cuenta = 0
cadena = "Chupa la pichula"
for l in cadena:
    if l == "l":
        cuenta += 1
print(cuenta)

# Usando "in" para ver si un string contiene otro string.
vocales = "AÁaáEÉeéIÍiíoOÓóuUúÚ"
frase = "Tengo 9 vocales á é í ó"

cuenta = 0
for l in frase:
    if l in vocales:
        cuenta += 1
print(cuenta)

# Reverso de una cadena: [::-1] --> Desde el principio, hasta el final, con salto -1
print(nombre[::-1])
