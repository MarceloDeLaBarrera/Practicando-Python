import requests
import json

url = "https://httpbin.org/get"
response = requests.get(url)

if response.status_code == 200:
    content = response.content.decode("utf-8")
    data = response.json()
    datajson = json.loads(response.text)

# 3 formas de hacer lo mismo.
# print(content)
# print(data)
# print(datajson)

# Enviar parametros en la Url.
args = {"nombre": "Marcelo", "curso": "Python"}
response = requests.get(url, params=args)
data = response.json()
# print(data)

# el metodo get se encarga de pasar los parametros a la url, por lo que al printear response.url, se imprime la url con los parametros incluidos.
url_nueva = response.url

# ------------------------------------------------------------------------------------------------------------------------------------

# METODO POST.. Enviar informacion al servidor.
url = "https://httpbin.org/post"
# Payload es como se suele llamar al contenido de lo que enviaremos al servidor.
payload = {"nombre": "Marcelo", "curso": "Python"}

# Trabajar con encabezados:
headers = {"Content-type": "application/json", "access-token": "12345"}

# Tambien se puede hacer como--> requests.post(url, data=json.dumps(payload)) , ya que dumps se encarga de arrojar/lanzar el diccionario a json.
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    dictcondata = response.json()
    print(dictcondata)

# Obtiene, lee e imprime solo los headers.
print(response.headers)

"""Cuando se obtiene una conexion mediante una response, la conexion se cierra automaticamente. Para mantenerla abierta, se utiliza stream, pero requiere cerrar la conexion con .close() al final"""
