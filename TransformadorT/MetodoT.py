class Transformador:
    def __init__(self, string: str, tipo: int):
        self.string = string
        self.tipo = tipo

    def transformar(self, string:str, tipo: int):
        pass


class MetodoT(Transformador):
    def __init__(self, string: str, tipo: int):
        super().__init__(string, tipo)

        if self.tipo == 1:
            self.metodo1()
        elif self.tipo == 2:
            self.metodo2()
        elif self.tipo == 3:
            self.metodo3()

    def metodo1(self):
        return self.string.replace(" ", "-")

    def metodo2(self):
        return " ".join(self.string)

    def metodo3(self):
        return self.string.upper()
    

