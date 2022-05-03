class Producto():

    # variable de clase
    contador_productos = 0

    # Metodo constructor
    def __init__(self, nombre, precio, marca="Ferrero"):

        # Llamando y seteando a la variable de clase dentro del constructor.
        Producto.contador_productos += 1
        # Atributos
        self._idproducto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
        self._marca = marca

    # Metodos Get y Set

    def get_idroducto(self):
        return self._idproducto

    def set_idproducto(self, id):
        self._idproducto = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nom):
        self._nombre = nom

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, pre):
        self._precio = pre

    def __str__(self):
        return f"Id producto: {self._idproducto} - Nombre: {self._nombre} - Precio: {self._precio} -Marca: {self._marca}"


class Orden():

    # variable de clase
    contador_ordenes = 0

    # Constructor
    def __init__(self, list_prod):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(list_prod)

    # Metodos

    def agregar_producto(self, prod):
        self._productos.append(prod)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            # Se accede al objeto producto, metodo get precio, para capturar precio.
            total += producto.precio

        return total

    def __str__(self):
        producto_str = ""
        for prod in self._productos:
            producto_str += prod.__str__()+" | "
        return f"Orden {self._id_orden}  \nProductos: {producto_str}"


p1 = Producto("Pantalon", 1000)
p2 = Producto("Camisa", 2000, "Armani")
listproductos = [p1, p2]
orden1 = Orden(listproductos)
print(orden1)
orden2 = Orden(listproductos)
print(orden2)
p3 = Producto("Corbata", 500)
orden2.agregar_producto(p3)
print(orden2)
print(f"Total Orden 2: {orden2.calcular_total()}")

p1.set_nombre("Pantalón")
print(orden1)

for orden in orden1:
    print(orden)
