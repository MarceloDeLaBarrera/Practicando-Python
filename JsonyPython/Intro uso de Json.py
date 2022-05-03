import json

# json.dumps permite convertir un objeto en formato json.
# json.loads permite convertir un archivo o data json en formato python/diccionario.
# json.load permite recuperar info de un archivo.
# json.dump permite enviar info hacia un archivo.

diccionario = {
    "Personas": [
        {
            "Nombre": "Juan",
            "Edad": 24
        },
        {
            "Nombre": "Pedro",
            "Edad": 45
        }
    ]
}

string = "Mi mama me mima"

# Carga de diccionario a archivo Json. Forma1 (modo write):
with open("Prueba1_IntroUso_JsonconPython.json", "w") as archivo:
    json.dump(diccionario, archivo, indent=2)

# Leer desde archivo json. (Modo read)
with open("Prueba1_IntroUso_JsonconPython.json", "r") as archivo:
    datos = json.load(archivo)
print(type(datos))

for persona in datos["Personas"]:
    print(persona["Nombre"])
