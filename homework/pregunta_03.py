"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def reducer(sequence):
    """Reducer"""
    diccionario = {}
    for key, value in sequence:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    return list(diccionario.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [(line[0], int(line[1])) for line in fileInformation]

    lettersCountSeparated = sorted(lettersCountSeparated)

    lettersCountSeparated = reducer(lettersCountSeparated)

    return lettersCountSeparated


pregunta_03()
