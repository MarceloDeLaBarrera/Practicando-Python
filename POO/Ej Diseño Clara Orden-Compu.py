class DispositivoEntrada():
    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipoentrada = tipo


class Raton(DispositivoEntrada):

    # Variable de clase
    contador_ratones = 0

    def __init__(self, marca, tipo):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo)

    def __str__(self):
        # Accediendo directamente a atributos de la clase padre sin metodo get.
        return f"ID: {self._id_raton} - Marca: {self._marca} - Tipo Entrada: {self._tipoentrada}"


class Teclado(DispositivoEntrada):

    # Variable de clase
    contador_teclados = 0

    def __init__(self, marca, tipo):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo)

    def __str__(self):
        # Accediendo directamente a atributos de la clase padre sin metodo get.
        return f"ID: {self._id_teclado} - Marca: {self._marca} - Tipo Entrada: {self._tipoentrada}"


class Monitor():

    # Variable de clase
    contador_monitores = 0

    def __init__(self, marca, tamanno):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanno = tamanno

    def __str__(self):
        return f"ID: {self._id_monitor} - Marca: {self._marca} - Tamaño: {self._tamanno} pulgadas."


class Computadora():
    # Variable de clase
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"Computadora: ID: {self._id_computadora} - Nombre: {self._nombre} \nMonitor: {self._monitor} - \nTeclado: {self._teclado} - \nRaton: {self._raton}"


class Orden():
    # Variable de clase
    contador_ordenes = 0

    def __init__(self, lista):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._lista_computadora = lista

    def agregar_computadora(self, computadora):
        self._lista_computadora.append(computadora)

    def __str__(self):
        pcstr = ""
        for pc in self._lista_computadora:
            pcstr += "\n" + pc.__str__() + "\n"
        return f"Orden n°{self._id_orden} - Detalle Pedido: \n{pcstr}"


r1 = Raton("Marquita", "USB")
t1 = Teclado("HP", "USB")
m1 = Monitor("Gigabyte", 27)
c1 = Computadora("Asus Gx726", m1, t1, r1)
r2 = Raton("Nexus", "Bluetooth")
t2 = Teclado("Access", "USB")
m2 = Monitor("LG", 52)
c2 = Computadora("LG Hff272", m2, t2, r2)

listapcs = [c1, c2]

o1 = Orden(listapcs)
print(o1)
