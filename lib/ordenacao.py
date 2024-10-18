
def bubble_sort(lista: list) -> None:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] > lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
    return lista