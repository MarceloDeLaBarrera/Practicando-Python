import requests

baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"


# Retorna la responsejson para una determinada pagina "x"
def main_request(base, endp, x):
    response = requests.get(base+endp + f"?page={x}")
    d = response.json()
    return d


def main_request2(url):
    response = requests.get(url)
    d = response.json()
    return d

# Obtiene el numero de paginas desde la responsejson.


def get_pages(responsejson):
    pages = responsejson["info"]["pages"]
    return pages

# Extrae datos de la response json y los almacena como diccionario dentro de una lista.


def stract_data(responsejson):
    charlist = []
    for char in responsejson["results"]:
        character = {
            "id": char["id"],
            "name": char["name"],
            "episodes": len(char["episode"])
        }
        charlist.append(character)
    return charlist


data = main_request(baseurl, endpoint, 1)
pages = get_pages(data)

# Recorre desde 1 hasta la pagina 34 o hasta pagina que se le indique, realizando la request para obtener la responsejson, extrayendo los datos de la pagina de turno, y extendiendo la lista vacia con esos datos en cada vuelta.


def total_elements(pages):
    new_list = []
    for i in range(1, pages+1):
        data = main_request(baseurl, endpoint, i)
        charxpage = stract_data(data)
        new_list.extend(charxpage)
    return new_list


newlist = total_elements(34)
# print(len(newlist))


url = baseurl+endpoint+f"?page={1}"
# Recorriendo por nextpage.


def total_elements2(url):
    new_list = []

    # Mientras que la url exista:
    while url:
        data = main_request2(url)
        # Actualizar la url con el valor de next en cada vuelta del ciclo while.
        url = data["info"]["next"]
        charxpage = stract_data(data)
        new_list.extend(charxpage)
    return new_list


newlist = total_elements2(url)
print(len(newlist))
