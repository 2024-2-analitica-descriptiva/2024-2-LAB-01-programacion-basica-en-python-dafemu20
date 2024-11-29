"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def obtenerValorMayorYMenor(sequence):
    """
    Retorna el valor mayor y menor de una secuencia de numeros.

    Parameters:
    sequence: list
        Lista de numeros.

    Returns:
    tuple
        Tupla con el valor mayor y menor de la secuencia.
    """
    groupedData = {}
    for letter, number in sequence:
        if letter not in groupedData:
            groupedData[letter] = []
        groupedData[letter].append(number)

    tuplasMinimosMaximos = []
    for letter in groupedData.keys():
        (maximo, minimo) = (max(groupedData[letter]), min(groupedData[letter]))
        tuplasMinimosMaximos.append((letter, int(maximo), int(minimo)))

    return tuplasMinimosMaximos


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [(line[0], line[1]) for line in fileInformation]

    lettersCountSeparated = sorted(lettersCountSeparated)

    lettersCountSeparated = obtenerValorMayorYMenor(lettersCountSeparated)

    return lettersCountSeparated


pregunta_05()
