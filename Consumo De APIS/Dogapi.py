import json
import requests


# ------------------------PROBANDO API DOGS----------------------
url = "https://docs.thedogapi.com/"
api_key = "fb3ae2bf-f29c-45e7-89d4-0464771baada"
response = requests.get(
    f"https://api.thedogapi.com/v1/breeds?api_key={api_key}")
dog_data = response.json()

total_dogs = response.headers["pagination-count"]
headers = response.headers
print(headers)
count = 0
for id in dog_data:
    count += 1
print(count)
print(total_dogs)
print(len(dog_data))


frecuency_breedgroup = {}

for breedgroup in dog_data:
    # Como no todos los diccionarios traen una key "breed_group", arroja error si no se aplica .get. Value almacena valor de la key, si no la encuentra asigna valor NONE.
    value = breedgroup.get("breed_group", None)
    if value in frecuency_breedgroup:
        frecuency_breedgroup[value] += 1
    else:
        frecuency_breedgroup[value] = 1

print(frecuency_breedgroup)


def Mayor(diccionario):

    maximo = 0
    for i in diccionario:
        if diccionario[i] > maximo:
            maximo = diccionario[i]
            p = i

    return p


most_common_breedgroup = Mayor(frecuency_breedgroup)
print(most_common_breedgroup)


# Accediendo a un registro por id.
response = requests.get(
    f"https://api.thedogapi.com/v1/breeds/1?api_key={api_key}")
dog_data = response.json()


# Limitar registros.
response = requests.get(
    f"https://api.thedogapi.com/v1/breeds?limit=10&page=0?api_key={api_key}")
dog_data = response.json()

# Obtener random:
response = requests.get(
    f"https://api.thedogapi.com/v1/images/search?api_key={api_key}")
dog_data = response.json()
# print(dog_data)


url = f"https://api.thedogapi.com/v1/votes?api_key={api_key}"
payload = {"image_id": "10",
           "sub_id": "my-user",
           "value": 1
           }

response = requests.post(url, json=payload)
data = response.json()
print(data)
