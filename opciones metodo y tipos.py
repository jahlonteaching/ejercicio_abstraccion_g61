def main():
    print("Bienvenido al programa de transformaciones.")
    print("Por favor, elige un método de transformación:")
    print("1. Método 1")
    print("2. Método 2")
    print("3. Método 3")
    print("4. Método 4")

    metodo_elegido = int(input("Ingresa el número del método deseado: "))

    if metodo_elegido in range(1, 5):
        tipos_de_transformacion(metodo_elegido)
    else:
        print("Opción no válida. Por favor, elige un método del 1 al 4.")

def tipos_de_transformacion(metodo):
    print(f"Has elegido el Método {metodo}.")
    print("Por favor, selecciona un tipo de transformación:")
    print("1. Tipo de Transformación 1")
    print("2. Tipo de Transformación 2")
    print("3. Tipo de Transformación 3")
    print("4. Tipo de Transformación 4")

    tipo_elegido = int(input("Ingresa el número del tipo de transformación deseado: "))

    if tipo_elegido in range(1, 5):
        # Aquí puedes implementar la lógica específica para cada tipo de transformación.
        print(f"Has elegido el Tipo de Transformación {tipo_elegido}.")
    else:
        print("Opción no válida. Por favor, elige un tipo del 1 al 4.")

if __name__ == "__main__":
    main()
