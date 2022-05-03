# Ejemplo forma clasica:
lista = []
for n in range(1, 6):
    lista.append(n)
print(lista)

# Lista por comprension:
lista2 = [n for n in range(1, 6)]
print(lista2)

elevados = [n**2 for n in lista2]
print(elevados)

# Si lleva un else, todo el condicional va antes del bucle for.
pares = [n for n in lista2 if n % 2 == 0]
print(pares)

# Forma clasica
cadena = "mama"
letras = []
for l in cadena:
    letras.append(l)
print(letras)

# Por compresion:
letrass = [l for l in cadena]
print(letrass)

# Numero siguiente a un multiplo de 7 u 11.
listax = [n+1 for n in range(1, 31) if n % 7 == 0 or n % 11 == 0]
print(listax)

valores = [1.244343, 1.2434343, 1.2546575, 5.432423, 6.65234]
valores_redondeados = [round(v, 2) for v in valores]
print(valores_redondeados)

palabras = ["pepe", "jaja", "chupatula", "comemierda"]
palabras_mayus = [p.upper() for p in palabras]
print(palabras_mayus)

lista_cartesiana = [(i, j) for i in range(1, 6) for j in range(1, 6)]
print(lista_cartesiana)

listan = [2, 3, 5]
listan2 = [2, 4, 6]
listan3 = [1, 3, 4]

lista_for_suma = [(i+j+k)
                  for i in listan for j in listan2 for k in listan3 if i+j+k > 10]
print(lista_for_suma)
