from transformacion.modelo.abstracciones import Transformador
from transformacion.modelo.transformaciones import MetodoArroba, MetodoT


def main():
    print("Bienvenido al programa de transformaciones.")
    print("Por favor, elige un método de transformación:")
    print("1. Método 1")
    print("2. Método 2")
    print("3. Método 3")
    print("4. Método 4")

    metodo_elegido = int(input("Ingresa el número del método deseado: "))

    transformador: Transformador = obtener_metodo_transformacion(metodo_elegido)

    texto = input("Ingrese el texto a transformar")
    tipo = tipos_de_transformacion()


    texto_transformado = transformador.transformar(texto, tipo)

    print(f"Texto transformado: {texto_transformado}")


def tipos_de_transformacion():
    print("Por favor, selecciona un tipo de transformación:")
    print("1. Tipo de Transformación 1")
    print("2. Tipo de Transformación 2")
    print("3. Tipo de Transformación 3")

    tipo_elegido = int(input("Ingresa el número del tipo de transformación deseado: "))
    return tipo_elegido


def obtener_metodo_transformacion(metodo: int) -> Transformador:
    if metodo == 1:
        return MetodoArroba()

    if metodo == 2:
        return MetodoT()

    if metodo == 3:
        pass

    if metodo == 4:
        pass

    raise ValueError


if __name__ == "__main__":
    main()
