class Tuki:

    def text_reversed(self, text: str):
        text: str = ''.join(reversed(text))
        return text

    def text_upper(self, text: str):
        text: str = text.upper()
        return text

    def text_lower(self, text: str):
        text: str = text.lower()
        return text

    def transformar(self, string: str, type: int) -> str:
        if type == 1:
            return self.text_reversed(string)
        elif type == 2:
            return self.text_upper(string)
        elif type == 3:
            return self.text_lower(string)