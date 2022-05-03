# Se utiliza para comparar objetos, ya que pueden estar construidos por muchos atributos, y permite que Python identifique cual atributo es el que se esta comparando.

class Peliculas():
    def __init__(self, tit, dir, anio, dur):
        self._titulo = tit
        self._director = dir
        self._anno = anio
        self._duracion = dur

    def __str__(self):
        return f"Titulo: {self._titulo}\nDirector: {self._director}\nAño: {self._anno}\nDuracion: {self._duracion} "

    # Less than (menor que)
    def __lt__(self, comparador):
        # return self._titulo < comparador._titulo
        return self._anno < comparador._anno

    # Equal, igual que.
    def __eq__(self, comparador):
        return self._titulo == comparador._titulo and self._anno == comparador._anno

    # Less Equal than (Menor igual que)
    def __le__(self, comparador):
        return self == comparador or self < comparador

    # Great than (mayor que)
    def __gt__():
        pass

    # Great Equal than (Mayor igual que)
    def __ge__():
        pass

    # Add sumar
    def __add__(self, element):
        return f"Titulo: {self._titulo}\nDirector: {self._director}\nAño: {self._anno+element}\nDuracion: {self._duracion} "
        # eturn self._anno + element._anno

    # sub restar
    def __sub__():
        pass
    # Multiplicar

    def __mul__():
        pass
    # elevar

    def __pow__():
        pass
    # dividir

    def __truediv__():
        pass


listapeliculas = []
listapeliculas.append(
    Peliculas("El Padrino", "Francis Ford Coppola", 1972, 175))
listapeliculas.append(Peliculas("Toro Salvaje", "Martin Scorsese", 1980, 129))
listapeliculas.append(Peliculas("CasaBlanca", "Michael Curtiz", 1942, 200))
listapeliculas.append(Peliculas("CasaBlanca", "Michael Curtiz", 1942, 200))
listapeliculas.append(Peliculas("Asadito", "Jorguito", 1979, 200))

# Gracias a la sobrecarga del __lt__ permite hacer el sort de los objetos dentro de la lista.
listapeliculas.sort()

for pelicula in listapeliculas:
    print(pelicula)
    print("-"*20)


def director_sort(dir):
    return dir._director


print("**********************************")
listapeliculas = sorted(listapeliculas, key=director_sort)

for pelicula in listapeliculas:
    print(pelicula)
    print("-"*20)

print(listapeliculas[0] == listapeliculas[1])
print(listapeliculas[0] < listapeliculas[1])
print(listapeliculas[2]+5)
# print(listapeliculas[0]+listapeliculas[1])
