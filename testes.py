from lib.ordenacao import *

listas = [
    {
        "original": [5, 2, 9, 1, 5, 6],
        "ordenada": [1, 2, 5, 5, 6, 9]},
    {
        "original": [10, 80, 30, 90, 40, 50, 70],
        "ordenada": [10, 30, 40, 50, 70, 80, 90],
    },
]

for lista in listas:
    lista_copiada = lista["original"].copy()
    selection_sort(lista_copiada)
    assert lista_copiada == lista["ordenada"]