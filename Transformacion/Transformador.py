import re

class InvertirString:
    def invertir_cadena(self, cadena: str) -> str:

        cadena_invertida = ""
        for caracter in reversed(cadena):
            cadena_invertida += caracter
        return cadena_invertida

    def invertir_numero(self, numero: int) -> int:

        if numero == 0:
            return 0
        else:
            digitos = str(numero)
            digitos_invertidos = digitos[::-1]
            numero_invertido = int(digitos_invertidos)
            return numero_invertido


class RemoverCaracteresEspeciales:
    def __init__(self, data):
        self.data = data

    def remove_special_characters(self):
        if isinstance(self.data, str):
            self.data = re.sub(r'[^a-zA-Z0-9\s]', '', self.data)
        elif isinstance(self.data, int):
            self.data = str(self.data)
            self.data = re.sub(r'[^0-9]', '', self.data)
        else:
            raise TypeError("Solo se admiten strings o enteros")