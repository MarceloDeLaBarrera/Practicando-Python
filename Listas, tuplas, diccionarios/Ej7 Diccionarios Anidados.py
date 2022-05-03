
# Diccionario que contiene diccionarios como valores en las claves del primer diccionario.
agenda = {
    "Jorge": {
        "Telefono": 11111,
        "Pais": "Ecuador",
        "Personal": {
            "Aficion": "Astronomia",
            "Estudios": "Ciencias",
            "Musica": "Clasica"
        }
    },

    "Maria": {
        "Telefono": 2222,
        "Pais": "Colombia",
        "Personal": {
            "Aficion": "Futbol",
            "Estudios": "Agronomia",
            "Musica": "Rock"
        }
    },

    "Tomas": {
        "Telefono": 3333,
        "Pais": "España",
        "Personal": {
            "Aficion": "Ajedrez",
            "Estudios": "Informatica",
            "Musica": "Pop"
        }
    },

    "Carla": {
        "Telefono": 4444,
        "Pais": "Mexico",
        "Personal": {
            "Aficion": "Atletismo",
            "Estudios": "Matematicas",
            "Musica": "Reggaeton"
        }
    }
}

pais_maria = agenda["Maria"]["Pais"]
print(pais_maria)

aficiones_carla = agenda["Carla"]["Personal"]


# Imprimir todo el contenido del diccionario.
for clave, valor in agenda.items():
    print(f"{clave}: {valor}")

for nombre in agenda:
    print(nombre)
    for datos in agenda[nombre]:
        print(f"{datos}: {agenda[nombre][datos]}")

# Imprimir nombre y pais. OJO: Funciona solo con una comilla al pasar la clave pais.
for clave, valor in agenda.items():
    print(f"{clave}: {valor['Pais']}")

# Comprobar si alguien es de Mexico y le gusta el reggaeton.
for clave, valor in agenda.items():
    if valor['Pais'] == "Mexico" and valor["Personal"]["Musica"] == "Reggaeton":
        print(f"A {clave} le gusta el Reggaeton y es de Mexico ")
        break
    else:
        print(f"Los datos no coinciden con {clave}")

# Mostrar todos los datos personales de cada miembro

for nombre, datos in agenda.items():
    print(f"Datos personales de {nombre}: ")
    for categoria, informacion in datos['Personal'].items():
        print(f"- {categoria}: {informacion}")


# Lista con diccionarios en su interior
lista = [{"Nombre": "Jorge", "Color": "Rojo"}, {"Nombre": "Pedro", "Color": "Rojo"},
         {"Nombre": "Ramon", "Color": "Verde"}, {
             "Nombre": "Ramon", "Color": "Rojo"},
         {"Nombre": "Ramon", "Color": "Verde"}, {
             "Nombre": "Ramon", "Color": "Rojo"},
         {"Nombre": "Ramon", "Color": "Verde"}]

frecuencydict = {}

# Recorrer claves de diccionario dentro de lista y capturar su valor.
for dict in lista:
    if dict["Color"] not in frecuencydict:
        frecuencydict[dict["Color"]] = 1
    else:
        frecuencydict[dict["Color"]] += 1

print(frecuencydict)

# Lista con diccionarios que contienen diccionarios.
lista2 = [{"Persona1": {"Nombre": "Jorge", "Color": "Rojo"}}, {"Persona2": {"Nombre": "Pedro", "Color": "Rojo"}},
          {"Persona3": {"Nombre": "Ramon", "Color": "Verde"}}, {
              "Persona4": {"Nombre": "Ramon", "Color": "Rojo"}},
          {"Persona5": {"Nombre": "Ramon", "Color": "Verde"}}, {
              "Persona6": {"Nombre": "Ramon", "Color": "Rojo"}},
          {"Persona7": {"Nombre": "Ramon", "Color": "Verde"}}]

frecuencydict2 = {}

# Recorrer diccionarios en lista, y a su vez, recorrer los diccionarios que estan dentro de los diccionarios, accediendo a los valores y capturandolos.
for dict in lista2:
    for c, v in dict.items():
        if v["Color"] not in frecuencydict2:
            frecuencydict2[v["Color"]] = 1
        else:
            frecuencydict2[v["Color"]] += 1

print(frecuencydict2)
