
class Ingredientes():

    id_ingrediente = 0

    def __init__(self, nom, cant, unid):
        Ingredientes.id_ingrediente += 1
        self._id_ingrediente = Ingredientes.id_ingrediente
        self._nombre = nom
        self._cantidad = cant
        self._unidad = unid

    def __str__(self):
        return f"Ingrediente {self._id_ingrediente} - Nombre: {self._nombre} - Cantidad: {self._cantidad} - Unidad: {self._unidad}"


class Receta():

    # variable de clase
    contador_recetas = 0

    # Constructor
    def __init__(self, lista, nombre):
        Receta.contador_recetas += 1
        self._id_receta = Receta.contador_recetas
        self._nombre = nombre
        self._lista_ingredientes = list(lista)

    def __str__(self):
        ingredientes_str = ""
        for ingr in self._lista_ingredientes:
            ingredientes_str += "\n" + ingr.__str__()

        return f"Receta N{self._id_receta}  |  Nombre: {self._nombre} \nLista de ingredientes: {ingredientes_str}"

    def agregar_ingredientes(self, ingr):
        self._lista_ingredientes.append(ingr)

    def consultar_ingredientes(self):
        for ingr in self._lista_ingredientes:
            print(ingr)


ingr1 = Ingredientes("Jamon", 20, "gr")
ingr2 = Ingredientes("Queso", 50, "gr")
ingr3 = Ingredientes("Tomate", 100, "gr")
lista = [ingr1, ingr2, ingr3]
print(ingr1)
print(ingr2)

receta1 = Receta(lista, "Pizza")
receta2 = Receta(lista, "Pizza")
print(receta1)
print(receta2)
