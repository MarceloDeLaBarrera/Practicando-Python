import requests


# -------------------PROBANDO API CATS----------------------
url = "https://docs.thecatapi.com/"
api_key = "e565565c-046c-474b-a56c-190d7e0faa8b"
# response almacena un codigo de respuesta. Un response.
response = requests.get(
    f"https://api.thecatapi.com/v1/breeds?api_key={api_key}")
# response.json trae el json de la request en forma de diccionario.
cat_data = response.json()
# print(cat_data)
# content entrega el contenido pero en bytes, por lo que para transformarlo hay que aplicarle un decode.
content = response.content.decode("utf-8")
print("\n-----------------------------------------------------------------------------------------\n")
# print(content)


count = 0
for cat in cat_data:
    results = cat.get("name", None)
    if results:
        name = cat["name"]
        count += 1
print(count)


total_breeds = len(cat_data)
# response.headers muestra los headers de la request.
headers = response.headers
print(headers)
total_breeds2 = response.headers["pagination-count"]
print(total_breeds2)
