def bubble_sort(lista):
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

def selection_sort(lista: list) -> None:
    n = len(lista)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    print(lista)
    
