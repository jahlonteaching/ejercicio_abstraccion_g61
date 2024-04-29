from abc import ABC, abstractmethod


class Transformador(ABC):

    @abstractmethod
    def transformar(self, texto: str, tipo: int) -> str:
        ...
