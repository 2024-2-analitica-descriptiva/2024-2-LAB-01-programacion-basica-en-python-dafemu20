"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.split("\t") for line in fileInformation]

    lettersCountSeparated = [line[4].split(",") for line in fileInformation]
    lettersCountSeparated = [
        item.split(":") for sublist in lettersCountSeparated for item in sublist
    ]

    groupedData = {}
    for letter, number in lettersCountSeparated:
        if letter not in groupedData:
            groupedData[letter] = []
        groupedData[letter].append(int(number))

    resultado = {}
    for letter in groupedData.keys():
        resultado[letter] = len(groupedData[letter])

    return resultado

pregunta_09()
