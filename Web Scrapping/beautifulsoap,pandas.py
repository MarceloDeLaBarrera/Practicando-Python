from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"


def connect(url):
    response = requests.get(url)
    data = response.content

    # html.parser para que interprete como html
    soup = BeautifulSoup(data, "html.parser")
    return soup


# Equipos

soup = connect(url)
# con find all, busca todos los tipo span, con clase nombre-equipo, y devuelve todo el codigo html asociada a esa busqueda, con el etiqueado.
equiposhtml = soup.find_all('span', class_="nombre-equipo")

equipos = list()

count = 0
for i in equiposhtml:
    if count < 20:
        equipos.append(i.text)
    count += 1

print(equipos)

puntoshtml = soup.find_all('td', class_="destacado")

puntos = list()

count = 0
for i in puntoshtml:
    if count < 20:
        puntos.append(i.text)
    count += 1

print(puntos)

# Generando un dataframe, se utiliza diccionario para generarlo, y se le pasa un index que parta de 1 a 20 porque por defecto parte en 0.
df = pd.DataFrame({"Nombre": equipos, "Puntos": puntos},
                  index=list(range(1, 21)))
print(df)

absolute_path = os.path.abspath(__file__)
directory = os.path.dirname(absolute_path)
fullpath = os.path.join(directory, 'data/PuntosxEquipo.csv')


def generate_csv(df, fullpath):
    # Generar csv
    df.to_csv(fullpath, index=False)


url = "https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YZc4adDMIuU"

soup = connect(url)

week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

period_name = [period.find(class_="period-name").get_text()
               for period in items]
short_desc = [desc.find(class_="short-desc").get_text() for desc in items]
temperature = [temp.find(class_="temp").get_text()
               for temp in items if temp.find(class_="temp") != None]

print(period_name, short_desc, temperature)

df_weather = pd.DataFrame(
    {"Period": period_name, "Description": short_desc, "Temperature": temperature})
print(df_weather)
fullpath = os.path.join(directory, 'data/wheater.csv')
generate_csv(df_weather, fullpath)
