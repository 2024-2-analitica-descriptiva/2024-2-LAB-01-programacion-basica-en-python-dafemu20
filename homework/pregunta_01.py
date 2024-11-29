"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [line[0] for line in fileInformation]
    lettersCountSeparated = [(word, 1) for word in lettersCountSeparated]
    sumValues = sum([int(line[1]) for line in fileInformation])
    return sumValues


pregunta_01()
