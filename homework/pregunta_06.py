"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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

    tuplasMinimosMaximos = []
    for letter in groupedData.keys():
        (maximo, minimo) = (max(groupedData[letter]), min(groupedData[letter]))
        tuplasMinimosMaximos.append((letter, int(minimo), int(maximo)))

    tuplasMinimosMaximos = sorted(tuplasMinimosMaximos)

    return tuplasMinimosMaximos


pregunta_06()
