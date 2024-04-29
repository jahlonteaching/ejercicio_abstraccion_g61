class MetodoT(Transformador):

    def transformar(self, string:str, tipo: int):
        if tipo == 1:
            return self.fillspaces(string)
        elif tipo == 2:
            return self.mayus(string)
        elif tipo == 3:
            return self.hyphentospaces(string)


def fillspaces(string:str):
    return string.replace(" ", "-")

def mayus(string:str):
    return string.upper()

def hyphentospaces(string:str):
    return string.replace("-", " ")