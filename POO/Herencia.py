# Clase padre Vehiculos
class Vehiculos():
    # Constructor y atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    # Metodos
    def arrancar(self):
        self.enmarcha = True

    def frenar(self):
        self.frena = True

    def acelerar(self):
        self.acelera = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")


# Clase hijo, hereda de Vehiculos.
class Moto(Vehiculos):

    caballo = ""

    def __init__(self, marc, model, valor):
        self.valor = valor

        # super llama al constructor de la clase padre y asi se accede a sus atributos sin tener que declarar de 0 las mismas variables en clase hija por ejemplo.
        super().__init__(marc, model)

    def parada(self):
        self.caballo = "Moto haciendo caballito"
        return self.caballo


# Herencia Multiple

# Otra clase padre
class V_electrico(Vehiculos):
    # Constructor
    def __init__(self, marcaelectr, modeloelectr):
        self.autonomia = 100
        # La funcion super llama al metodo constructor de la clase padre.
        super().__init__(marcaelectr, modeloelectr)

    # Metodos
    def cargarenergia(self):
        self.cargando = True

    def estadoo(self):
        # La funcion super llama al metodo estado de la clase padre.
        super().estado()
        print(f"Autonomia: {self.autonomia}")

    def haceralgo(self):
        # En este caso se esta usando directamente el atributo de la clase padre marca, sin necesidad de usar el super.
        print(f"El {self.marca} esta andando a 100 km/h ")

# Clase hijo con herencia multiple. Se da preferencia a la primera clase que se indique, es decir, se hereda el constructor de la primera clase.


class bicielectrica(V_electrico, Vehiculos):
    pass


moto1 = Moto("Daewoo", "CBR", 2000)
moto1.estado()
print("\n")
print(moto1.valor)
print(moto1.parada())
print("\n")
bici1 = bicielectrica("Hyundai", "kk232")
bici1.estadoo()
bici1.haceralgo()
