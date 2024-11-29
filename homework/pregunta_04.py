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


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [line[2].split("-")[1] for line in fileInformation]
    lettersCountSeparated = [(word, 1) for word in lettersCountSeparated]

    lettersCountSeparated = sorted(lettersCountSeparated)

    lettersCountSeparated = reducer(lettersCountSeparated)

    return lettersCountSeparated


pregunta_04()
