class Transformador:
    def transformar(self, string:str, tipo: int):
        pass


class MetodoT(Transformador):
    def __init__(self):
        super().__init__()

        if self.tipo == 1:
            self.metodo1()
        elif tipo == 2:
            self.metodo2()
        elif tipo == 3:
            self.metodo3()

    def metodo1(self):
        return self.string.replace(" ", "-")

    def metodo2(self):
        for letter in self.string:
            self.string.join(letter + " ")
    
    

