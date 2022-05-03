class Auto1():
    def __init__(self) -> None:
        pass

    def metodo1(self):
        print("Este es el metodo 1")
        return 1

    def metodo3(self):
        data = self.metodo1()
        print(f"Metodo1 llamado y retorna {data}")
        Aut2 = Auto2()
        data2 = Aut2.metodo2()
        print(f"Metodo2 ha sido llamado y retorna {data2}")


class Auto2():
    def __init__(self) -> None:
        pass

    def metodo2(self):
        print("Este es el metodo 2")
        return 2


obj_aut1 = Auto1()
obj_aut1.metodo3()
