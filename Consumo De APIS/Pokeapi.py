import requests


# ------------------------PROBANDO API Pokemon----------------------
documentacion = "https://pokeapi.co/docs/v2"
# limit= cuantos resultados se muestran
limit = "?limit=100"
# offset= cambiar de pagina.Desde que numero de pokemon en adelante empezar a contar
offset = "&offset=0"
limit = ""
offset = ""
url = "https://pokeapi.co/api/v2/pokemon/"
params = {"limit": 20}
#response = requests.get(f"{url}{limit}{offset}")
response = requests.get(url, params=params)
pokemon_data = response.json()
# print(pokemon_data)
headers = response.headers
print(headers)


# Acceder a un solo pokemon:
name = "charizard"
data = requests.get(
    f"https://pokeapi.co/api/v2/pokemon/{name}")
pokemon_data = data.json()

for p in pokemon_data["types"]:
    print(p["type"]["name"])


# CAPTURAR TODOS LOS DATOS CUANDO LA API ES PAGINADA, primera forma:
"""Solo funciona cuando se conoce la cantidad de paginas u offset. El total count."""
limit = 100
pokemon = []
for i in range(12):
    offset = i*100
    params = {"offset": offset, "limit": limit}
    response = requests.get(url, params=params)
    # Por cada vuelta pokemon_data almacena una lista con 100 resultados.
    pokemon_data = response.json()
    # Se usa extend en vez de apend, ya que append añadiria cada lista entera dentro de la lista, en cambio extends, añade de forma independiente los elementos dentro de una lista, puesto que itera los elementos.
    pokemon.extend(pokemon_data["results"])
    # Tambien se puede usar suma de listas, ya que eso une los elementos de la lista en una misma lista.
    #pokemon += pokemon_data["results"]

print(len(pokemon))
pokemon_names = []
for name in pokemon:
    pokemon_names.append(name["name"])
print(pokemon_names)

# CAPTURAR TODOS LOS DATOS CUANDO LA API ES PAGINADA, segunda forma:
"""Se recorre mediante la url next"""

url = "https://pokeapi.co/api/v2/pokemon/?limit=100"
pokemon = []

# Mientras que la url exista:
while url:
    response = requests.get(url)
    pokemon_data = response.json()
    # Actualizar la url con el valor de next en cada vuelta del ciclo while.
    url = pokemon_data["next"]
    pokemon.extend(pokemon_data["results"])

print(len(pokemon))


# CAPTURAR TODOS LOS DATOS CUANDO LA API ES PAGINADA, tercera forma:
"Se va recorriendo hasta que no queden mas offset"
offset = 0
url = f"https://pokeapi.co/api/v2/pokemon/?limit=100&offset={offset}"
pokemon = []

while True:
    response = requests.get(url)
    pokemon_data = response.json()
    offset = offset+100
    url = f"https://pokeapi.co/api/v2/pokemon/?limit=100&offset={offset}"
    if pokemon_data["results"] != []:
        pokemon.extend(pokemon_data["results"])
    else:
        break

print(len(pokemon))
# print(pokemon)


pokemon_names = []
pokemon_fotos = []
pokemon_types = []

for name in pokemon:
    pokemon_names.append(name["name"])
    name = name["name"]
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    pokemon_data = data.json()
    foto = pokemon_data['sprites']['other']['dream_world']['front_default']
    pokemon_fotos.append(foto)
    types = [t["type"]["name"] for t in pokemon_data["types"]]
    pokemon_types.append(types)

print(pokemon_fotos)
