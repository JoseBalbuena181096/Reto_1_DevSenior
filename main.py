
"""
Proyecto: Simulación de un proyecto de investigación cientifica en Python
Modulo 1 Dev Senior Code
Author: José Ángel Balbuena Palma
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
    categoria = input('Ingrese la categoria del experimento de las siguientes Quimica, Fisica o Biologia\n').strip().lower().capitalize()
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
        return
    if indice < 1 or indice > len(listaExperimentos):
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

def calcularEstadisticas(listaExperimentos):
    """ Calcular estadisticas basicas (promedios, maximos y minimos) de un experimentos, requiere de la funcion agregarExperimentos """
    if not listaExperimentos:
        print('No hay experimentos disponibles')
        return
    indice_str = input(f"Ingrese el ID del experimento a analizar estadisticas entre 1 y {len(listaExperimentos)}\n").strip()
    try:
        indice = int(indice_str)
    except ValueError:
        print("El indice no es numerico ")
        return
    if indice < 1 and indice > len(listaExperimentos):
        print("El ID del experimento esta fuera del rango de experimetos ")
        return
    experimento = listaExperimentos[indice-1]
    promedio = statistics.mean(experimento.resultados)
    maximo = max(experimento.resultados)
    minimo = min(experimento.resultados)
    tabla = PrettyTable()
    tabla.field_names = ["Promedio", "Maximo Valor", "Minimo Valor"]
    tabla.add_row([f'{promedio:.2f}',f'{maximo}', f'{minimo}'])
    print("Resultado experimentos: \n")
    print(tabla)

def compararExperimentos(listaExperimentos):
    """ Compara dos o mas experimentos para determinar los mejores o peores resutados, dificultad 2 requiere el uso de funciones calcularEstadisticas """
    if not listaExperimentos:
        print('No hay experimentos disponibles')
        return
    
    indicesComparacion_str = input(f"Ingrese la lista de IDs de los experimentos a comparar entre 1 y {len(listaExperimentos)}, separados por coma ej 1,3,4 \n").strip()
    try:
        indicesComparacion = list(map(int, indicesComparacion_str.split(','))) 
    except ValueError:
        print("Los indices no son númericos ")

    for indiceComparacion in indicesComparacion: 
        if indiceComparacion < 1 and indiceComparacion > len(listaExperimentos):
            print(f"El ID del comparacion {indiceComparacion} esta fuera del rango de experimetos\n ")
            return

    promedios = [] 
    maximos = []
    minimos =  []

    for indiceComparacion  in indicesComparacion:
        promedio = statistics.mean(listaExperimentos[indiceComparacion - 1].resultados)
        minimo = min(listaExperimentos[indiceComparacion - 1].resultados)
        maximo = max(listaExperimentos[indiceComparacion - 1].resultados)
        promedios.append([indiceComparacion-1 , promedio])
        minimos.append([indiceComparacion-1 , minimo])
        maximos.append([indiceComparacion-1 , maximo])

    # Ordemaniento de promedios, maximos y minimos
    promedios.sort(key=lambda promedio: promedio[1], reverse=True)
    maximos.sort(key=lambda maximo: maximo[1], reverse=True)
    minimos.sort(key=lambda minimo: minimo[1])

    tabla = PrettyTable()
    tabla.field_names = ["Estadistica", "Experimento", "Valor", "Categoria"]
    # Mejores
    tabla.add_row(['Promedio',f'{listaExperimentos[promedios[0][0]].nombre}', f'{promedios[0][1]}', 'Mejor'])
    tabla.add_row([' ',' ', ' ', ' '])
    tabla.add_row(['Maximo',f'{listaExperimentos[maximos[0][0]].nombre}', f'{maximos[0][1]}', 'Mejor'])
    tabla.add_row([' ',' ', ' ', ' '])
    tabla.add_row(['Minimo',f'{listaExperimentos[minimos[0][0]].nombre}', f'{minimos[0][1]}', 'Mejor'])
    tabla.add_row([' ',' ', ' ', ' '])
    # Peores
    tabla.add_row(['Promedio',f'{listaExperimentos[promedios[-1][0]].nombre}', f'{promedios[-1][1]}', 'Peor'])
    tabla.add_row([' ',' ', ' ', ' '])
    tabla.add_row(['Maximo',f'{listaExperimentos[maximos[-1][0]].nombre}', f'{maximos[-1][1]}', 'Peor'])
    tabla.add_row([' ',' ', ' ', ' '])
    tabla.add_row(['Minimo',f'{listaExperimentos[minimos[-1][0]].nombre}', f'{minimos[-1][1]}', 'Peor'])
    tabla.add_row([' ',' ', ' ', ' '])

    print("Comparación experimentos: \n")
    print(tabla)


def generaInforme(listaExperimentos):
    """ Generar un informe resumen de los experimentos y sus estadistica, dificultad 3 requiere el uso de funcuiones visualzarExperimento y calcularEstadisticas """
    if not listaExperimentos:
        print('No hay experimentos disponibles')
        return

    promedios = [] 
    maximos = []
    minimos =  []

    # Abrir un archivo txt para escribir un informe
    with open('informe_experimentos.txt', 'w') as archivo:
        archivo.write("ID, Nombre, Fecha experimento, Categoria, Resultados, Promedio, Maximo, Minimo" )
        archivo.write('\n')
        for id_, experimento in enumerate(listaExperimentos):
            promedio = statistics.mean(experimento.resultados)
            minimo = min(experimento.resultados)
            maximo = max(experimento.resultados)
            promedios.append([id_ , promedio])
            minimos.append([id_ , minimo])
            maximos.append([id_ , maximo])
            archivo.write(f'{id_+1} ,{experimento.nombre}, {experimento.fechaRealizacion.strftime('%d/%m/%Y')\
                            }, {experimento.categoria}, {experimento.resultados}, {promedio\
                            }, {maximo}, {minimo}\n')
            archivo.write('\n')

        # Ordemaniento de promedios, maximos y minimos
        promedios.sort(key=lambda promedio: promedio[1], reverse=True)
        maximos.sort(key=lambda maximo: maximo[1], reverse=True)
        minimos.sort(key=lambda minimo: minimo[1])

        archivo.write(f'El mejor promedio {listaExperimentos[promedios[0][0]].nombre} con {promedios[0][1]}')
        archivo.write('\n')
        archivo.write(f'El mejor maximo {listaExperimentos[maximos[0][0]].nombre} con {maximos[0][1]}')
        archivo.write('\n')
        archivo.write(f'El mejor minimo {listaExperimentos[minimos[0][0]].nombre} con {minimos[0][1]}')
        archivo.write('\n')
        archivo.write(f'El peor promedio {listaExperimentos[promedios[-1][0]].nombre} con {promedios[-1][1]}')
        archivo.write('\n')
        archivo.write(f'El peor maximo {listaExperimentos[maximos[-1][0]].nombre} con {maximos[-1][1]}')
        archivo.write('\n')
        archivo.write(f'El peor minimo {listaExperimentos[minimos[-1][0]].nombre} con {minimos[-1][1]}')
        archivo.write('\n')


    print('El informe generado como "informe_experimentos.txt "')    
            

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
        elif opcion == '4':
            calcularEstadisticas(listaExperimentos)
        elif opcion == '5':
            compararExperimentos(listaExperimentos)
        elif opcion == '6':
            generaInforme(listaExperimentos)
        elif opcion == '7':
            print('Fin del programa')
            break
        else:
            print('Opción incorrecta intente de nuevo\n')


if __name__ == "__main__":
    menu()
