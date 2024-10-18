def bubble_sort(lista: list) -> None:
    """Essa função organiza uma lista por Bubble sort"""
    
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista