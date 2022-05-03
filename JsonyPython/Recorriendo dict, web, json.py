import json
from urllib.request import urlopen

# Cargar archivo json
with open("states.json", "r") as file:
    data = json.load(file)

"""
for c, v in data.items():
    for element in v:
        print(element["name"], element["abbreviation"])
"""

for states in data["states"]:
    print(states["name"], states["abbreviation"])
    del states["area_codes"]


print(data)

with open("states_v2.json", "w") as file2:
    json.dump(data, file2, indent=2)

print(("\n"))

# Cargar json desde la web:
with urlopen("http://www.floatrates.com/daily/usd.json") as response:
    source = response.read()

# Convertir archivo json en formato python... Si viene en otro formato seria source.decode("UTF-8")
datos = json.loads(source)
print(datos)

for c, v in datos.items():
    print(v["name"], v["rate"])


for currency in datos:
    code = datos[currency]["code"]
    rate = datos[currency]["rate"]
    print(code, rate)


list = [{"perro": 3, "gato": 4}]

print(list[0]["perro"])
