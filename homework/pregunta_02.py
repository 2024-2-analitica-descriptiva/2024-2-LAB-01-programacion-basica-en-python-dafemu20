"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
import glob
import os.path
from itertools import groupby
import string


def reducer(sequence):
    """Reducer"""
    diccionario = {}
    for key, value in sequence:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    return list(diccionario.items())


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    fileInformation = open("files/input/data.csv", "r").readlines()
    fileInformation = [line.replace("\n", "") for line in fileInformation]
    fileInformation = [line.replace("\t", ",") for line in fileInformation]
    fileInformation = [line.split(",") for line in fileInformation]

    lettersCountSeparated = [line[0] for line in fileInformation]
    lettersCountSeparated = [(word, 1) for word in lettersCountSeparated]

    lettersCountSeparated = sorted(lettersCountSeparated)

    lettersCountSeparated = reducer(lettersCountSeparated)

    return lettersCountSeparated


pregunta_02()
