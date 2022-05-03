class Persona():
    # Constructor
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    # Metodos
    def descripcion(self):
        print(
            f"Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.lugar_residencia} ")


class Empleado(Persona):
    # Constructor
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        # atributos
        self.salario = salario
        self.antiguedad = antiguedad

        # La funcion super llama al metodo constructor de la clase padre.
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

    # Metodos
    def descripc(self):
        # super().descripcion()
        self.descripcion()
        print(f"Antiguedad: {self.antiguedad} \nSalario: {self.salario}")


Empleado1 = Empleado(15, 10, "Jose", "20", "Chile")
Empleado1.descripc()

# isinstance confirma si un objeto es pertenece a una clase.
print(isinstance(Empleado1, Empleado))
print(isinstance(Empleado1, Persona))
