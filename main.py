
"""
Atributos de un experimento: 
nombre, fecha(DD/MM/AAAA), tipo y resultados númericos
"""

from datetime import datetime 
import statistics
from prettytable import PrettyTable

categoriasExperimentos = ('Biologia', 'Fisica', 'Quimica')

class Experimento:
    """ Estructura basica de un experimento """
    def __init__(self, nombre, fechaRealizacion, categoria, resultados) -> None:
        # nombre del experimero str
        self.nombre = nombre
        # fecha del experimento formato DD/MM/AAAA
        self.fechaRealizacion = fechaRealizacion
        # categoria predefinida del experimento
        self.categoria = categoria
        # Lista de resultados númericos
        self.resultados = resultados



def agregarExperimento(listaExperimentos):
    """ Permite agregar un nuevo experimento con sus atributos , dificultad 1 no requiere nada"""
    nombre = input('Ingrese el nombre del experimento:\n').strip()
    if nombre == '':
        print('Nombre incorrecto ')
        return
    fechaExperimento_str = input('Ingrese la fecha del experimento: \n').strip()
    try:
        fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y")
    except ValueError:
        print('La fecha no valida')
        return
    categoria = input('Ingrese la categoria del experimento de las siguientes Quimica, Fisica o Biologia\n').strip().capitalize()
    if categoria == '' or not(categoria in categoriasExperimentos) :
        print('Categoria incorrecta ')
        return
    resultados_str = input('Ingrese los resultados del experimento separados por comas ejemplo 12.3,23.2,10\n')
    try:
        resultados = list(map(float, resultados_str.split(',')))
    except ValueError:
        print("Resultados en formato invalido ")
        return
    experimento = Experimento(nombre, fechaExperimento, categoria, resultados)
    listaExperimentos.append(experimento)
    print("El experimeto se agrego correctamente ")
    

def eliminarExperimentos(listaExperimentos):
    """ Perminte elimnar un experimento, dificultad 2 requiere de la funcion agregar """
    if not listaExperimentos:
        print('No hay experimentos disponibles')
        return
    indice_str = input(f"Ingrese el ID del experimento a eliminar entre 1 y {len(listaExperimentos)}\n").strip()
    try:
        indice = int(indice_str)
    except ValueError:
        print("El indice no es numerico ")
    if indice < 1 and indice > len(listaExperimentos):
        print("El ID del experimento esta fuera del rango de experimetos ")
        return
    eliminado = listaExperimentos.pop(indice-1)
    print(f'El experimeto {eliminado.nombre} se ha eliminado ')


def visualizarExperimentos(listaExperimentos):
    """ Permite agregar experimentos, dificultad 2 requiere uso de la funcion agregar """
    if not listaExperimentos:
        print('No hay experimentos disponibles')
        return 
    tabla = PrettyTable()
    # Definir columnas
    tabla.field_names = ["ID", "Nombre", "Fecha experimento", "Categoria", 'Resultados']
    for i, experimento in enumerate(listaExperimentos, start=1):
        tabla.add_row([f'{i}',f'{experimento.nombre}', f'{experimento.fechaRealizacion.strftime('%d/%m/%Y')}',\
                       f'{experimento.categoria}', f'{experimento.resultados}'])
        tabla.add_row([f' ',f' ', f' ', f' ', f' '])
    print("Experimentos:\n")
    print(tabla)

def calcularEstadisticas():
    """ Calcular estadisticas basicas (promedios, maximos y minimos) de un experimentos, requiere de la funcion agregarExperimentos """
    pass

def compararExperimentos():
    """ Compara dos o mas experimentos para determinar los mejores o peores resutados, dificultad 2 requiere el uso de funciones calcularEstadisticas """
    pass

def generaInforme():
    """ Generar un informe resumen de los experimentos y sus estadistica, dificultad 3 requiere el uso de funcuiones visualzarExperimento y calcularEstadisticas """
    pass

def menu():
    """ Menu principal del programa """ # Dificultad 3
    
    listaExperimentos = []
    
    while True:
        print("=== MENU PRINCIPAL ===\n")
        print("=== Gestión de experimentos  ===")
        print("1.  Agregar experimentos")
        print("2.  Visualizar experimentos")
        print("3.  Eliminar experimentos")
        print("=== Análisis de datos  ===")
        print("4.  Calcular estadisticas")
        print("5.  Comparar experimentos")
        print("=== Análisis de datos  ===")
        print("6.  Generar informe")
        print("=== Salir  ===")
        print("7.  Salir")
        opcion = input('Ingrese una opción del menu:\n')
        if opcion == '1':
            agregarExperimento(listaExperimentos)
        elif opcion == '2':
            visualizarExperimentos(listaExperimentos)
        elif opcion == '3':
            eliminarExperimentos(listaExperimentos)
        elif opcion == '7':
            print('Fin del programa')
            break
        else:
            print('Opción incorrecta intente de nuevo\n')


if __name__ == "__main__":
    menu()
