def bubble_sort(lista: list) -> None:
    x = len(lista)
    for i in range(x):
        sorteado = False
        for j in range(0, x-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                sorteado = True
        if not sorteado:
            break

def selection_sort(vector: list) -> None:
    for i in range(len(vector)): 
        min = i
        for j in range(i, len(vector)):
            if vector[j] < vector[min]:    
                min = j
        vector[min], vector[i] = vector[i], vector[min]