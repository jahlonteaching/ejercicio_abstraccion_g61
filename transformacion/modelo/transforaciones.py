class MetodoT(Transformador):

    def transformar(self, string:str, tipo: int):
        if tipo == 1:
            return self.metodo1(string)
        elif tipo == 2:
            return self.metodo2(string)
        elif tipo == 3:
            return self.metodo3(string)


def metodo1(string:str):
    return string.replace(" ", "-")

def metodo2(string:str):
    return " ".join(string)

def metodo3(string:str):
    return string.upper()