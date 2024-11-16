
"""
Atributos de un experimento: 
nombre, fecha(DD/MM/AAAA), tipo y resultados númericos
"""
# listaDeExperimentos = [
#     ["Experimento 1", "16/11/2024", "Quimica", [3,4,45,6 53] ]
# ]

def agregarExperimento():
    """ Permite agregar un nuevo experimento con sus atributos , dificultad 1 no requiere nada"""
    pass

def eliminarExperimentos():
    """ Perminte elimnar un experimento, dificultad 2 requiere de la funcion agregar """
    pass

def visualizarExperimentos():
    """ Permite agregar experimentos, dificultad 2 requiere uso de la funcion agregar """
    pass

def calcularEstadisticas():
    """ Calcular estadisticas basicas (promedios, maximos y minimos) de un experimentos, requiere de la funcion agregarExperimentos """
    pass

def compararExperimentos():
    """ Compara dos o mas experimentos para determinar los mejores o peores resutados, dificultad 2 requiere el uso de funciones calcularEstadisticas """
    pass

def generaInforme():
    """ Generar un informe resumen de los experimentos y sus estadistica, dificultad 3 requiere el uso de funcuiones visualzarExperimento y calcularEstadisticas """
    pass

def mostrarMenu():
    """ Muestra el menu principal del programa """ # Dificultad 3
    print("=== MENU PRINCIPAL ===")
    print("=== Gestión de experimentos  ===")
    print("1. Agregar experimentos")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    print("===  Análisis de datos  ===")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("===  Análisis de datos  ===")
    print("6. Generar informe")
    print("===  Salir  ===")
    print("7. Salir")



def main():
    """ Funcion que controla el flujo general del sistema, dificultad 1"""
    mostrarMenu()


if __name__ == "__main__":
    main()
