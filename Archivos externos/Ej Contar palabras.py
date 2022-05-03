# Mostrar que 5 palabras con mas de 12 letras aparecen mas veces, y cuantas veces aparece cada una.

txt = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\quijote.txt", "r", encoding="utf-8")

texto = txt.read()
txt.close()


# Otra forma seria (Primero convirtiendo luego spliteando y almacenando en lista.)
"""
quitar = "[],;:*-_+¿!?#%&/()=.\n!\"'"

for caracter in quitar:
    texto = texto.replace(caracter, " ")

texto = texto.lower()
palabras = texto.split()
"""

# Primero separando palabras en lista, y luego stripeandolas.
palabras = texto.split()

copial = list(palabras)
for letra in copial:
    if letra == " ":
        palabras.remove(letra)


frecuenciapalabras = {}

for palabra in palabras:
    palabra = palabra.strip(".").strip(",").strip(";").strip(
        ":").strip(" ").strip("!").strip("?").strip("¿").strip("!")
    if len(palabra) > 12:
        if palabra not in frecuenciapalabras:
            frecuenciapalabras[palabra] = 1
        else:
            frecuenciapalabras[palabra] += 1


# print(frecuenciapalabras)


def Mayor(diccionario):

    maximo = 0
    for i in diccionario:
        if diccionario[i] > maximo:
            maximo = diccionario[i]
            p = i

    return p, maximo


for i in range(5):
    for palabras in frecuenciapalabras:
        c, v = Mayor(frecuenciapalabras)
    print(f"{c} : {v}")
    del frecuenciapalabras[c]
