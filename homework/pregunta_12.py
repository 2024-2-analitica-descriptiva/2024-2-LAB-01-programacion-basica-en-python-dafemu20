"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", " ") for line in fileInformation]
    fileInformation = [line.split(" ") for line in fileInformation]
    fileInformation = [(line[0], line[4]) for line in fileInformation]
    fileInformation = [(line[0], line[1].split(",")) for line in fileInformation]

    groupedData = {}
    for letter, numbers in fileInformation:
        if letter not in groupedData:
            groupedData[letter] = []
        for number in numbers:
            groupedData[letter].append(int(number.split(":")[1]))

    resultado = {}
    for letter in groupedData.keys():
        resultado[letter] = sum(groupedData[letter])

    return resultado


pregunta_12()
