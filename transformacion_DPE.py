class TranformacionDPE(Transformador):
    def __init__(self):
        super().__init__()

    def transformar(self, s: str, tipo: int) -> str:
        if tipo == 1:
            str: str = s.replace(" ", "-")
            return str

        elif tipo == 2:
            str: str = s.lower()
            return str

        elif tipo == 3:
            str: str = s.lower()
            numeros = [(ord(letra) - ord("a") + 1) for letra in str if letra.isalpha()]
            str2 = ""
            for i in numeros:
                str2 += f" {i} "
            return str2