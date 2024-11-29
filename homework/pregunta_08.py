"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [(line[1], line[0]) for line in fileInformation]

    lettersCountSeparated = sorted(lettersCountSeparated, key=lambda x: x[0])

    lettersCountSeparated = [(line[0], line[1]) for line in lettersCountSeparated]

    lettersCountSeparated = [(line[0], [line[1]]) for line in lettersCountSeparated]

    indexMaped = sorted(list(set(map(lambda x: x[0], lettersCountSeparated))))

    resultado = []
    for index in indexMaped:
        valuesFiltered = list(filter(lambda x: x[0] == index, lettersCountSeparated))
        valuesLikeString = [value[1] for value in valuesFiltered]
        valuesFlattened = [item for sublist in valuesLikeString for item in sublist]
        resultado.append((int(index), sorted(set(valuesFlattened))))

    print(resultado)

    return resultado

pregunta_08()