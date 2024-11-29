"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", " ") for line in fileInformation]
    fileInformation = [line.split(" ") for line in fileInformation]
    fileInformation = [(line[1], line[3]) for line in fileInformation]
    fileInformation = [(line[0], line[1].split(",")) for line in fileInformation]

    groupedData = {}
    for number, letter in fileInformation:
        for letter in letter:
            if letter not in groupedData:
                groupedData[letter] = []
            groupedData[letter].append(int(number))

    resultado = {}
    for letter in groupedData.keys():
        resultado[letter] = sum(groupedData[letter])

    return resultado


pregunta_11()
