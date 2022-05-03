import os
import requests

"Descargar Json desde Url"

url = 'https://pokeapi.co/api/v2/pokemon/25'

response = requests.get(url)
data = str(response.json())

absolutepath = os.path.abspath(__file__)
base_dir = os.path.dirname(absolutepath)

#file = os.path.join(base_dir, 'pikachu.txt')
# with open(file, 'w') as pokedata:
#    pokedata.write(data)

"Descargar imagen desde url"
url = "https://fotografias.lasexta.com/clipping/cmsimages02/2020/09/21/86828440-B1FB-43AC-9E9C-A94AC6A4B8BD/default.jpg?crop=1300,731,x0,y0&width=1900&height=1069&optimize=low"

response = requests.get(url)
data = response.content
#file = os.path.join(base_dir, 'foto.jpg')
# with open(file, 'wb') as f:
#    f.write(data)
