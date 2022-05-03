import pandas as pd
import os
# Estructuras principales: Series y Dataframe.

serie = pd.Series([1, 2, 3])
print(serie)

df = pd.DataFrame({"columna1": [1, 2, 3, 4], "columna2": ["a", "b", "c", "d"]})
print(df)

# df.shape muestra la forma, es decir, cuantas filas y columnas tiene. En este caso, 4 filas y 2 columnas.
df.shape

# read permite leer un fichero desde una ubicacion dada.
absolute_path = os.path.abspath(__file__)
directory = os.path.dirname(absolute_path)
fullpath = os.path.join(directory, 'data/iris.data')
print(fullpath)
df = pd.read_csv(fullpath, header=None)

nombres = ["Longitud Sepalo", "Ancho Sepalo",
           "Longitud Petalo", "Ancho Petalo", "Clase"]
df.columns = nombres
df.index = list(range(1, 151))

# Muestra las primeras 5 filas, si se pone un numero dentro, mostrara hasta esa cantidad de filas.
dfhead = df.head()

# Muestra los ultimos 5, o los ultimos segun numero introducido.
dftail = df.tail()

# Describe() entrega una serie de datos de cada columna como min, max, etc.
datos = df.describe()
print(datos)

# value.counts, devuelve la cantidad de repeticiones de un item, en una determinada columna.
print(df["Clase"].value_counts())

print(df)

# Para transponer un dataframe
print(df.T)

# Para ordenar valores con sort. orden descendente-> Borrar el ascending.
print(df.sort_values("Ancho Sepalo", ascending=False))

# Seleccionar solo unas columnas
print(df[["Longitud Sepalo", "Longitud Petalo"]])

# Seleccionar solo unas filas
print(df[:8])

# df.iloc para devolver filas y columnas exactas. Ej
print(df.iloc[[4, 10], [0, 2]])

# Filtrar datos:
filtro = df[(df["Longitud Sepalo"] > 5) & (df["Longitud Petalo"] > 6.3)]
print(filtro)

# Operaciones entre columnas:
operacion = df["Longitud Sepalo"]-df["Longitud Petalo"]
print(operacion)

# Ver cuantos valores missing o perdidos hay.
missing = df.isna().sum()
print(missing)

# En caso de que hayan se rellenan con:
# df["<Campo con nulos>"].fillna(<valor con que se rellena>)

# Media
df["Longitud Petalo"].mean()

# mediana
df["Longitud Petalo"].median()

print(df)

# Operacion con lambda
# otro ejemplo lambda x: x**2 al cuadrado
dfminus = df["Ancho Petalo"].apply(lambda x: x**3)
print(dfminus)

# Devuelve la media, de cada una de las clases, de la columna ancho petalo.
dfgroupby = df.groupby("Clase")["Ancho Petalo"].mean()
dfgroupby.name = "Media ancho petalo agrupada x clase"
print(dfgroupby)
