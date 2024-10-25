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

def selection_sort(lista: list) -> list:
    for i in range(len(lista)):
        menor = i
        for k in range(i + 1, len(lista)):
            if lista[k] < lista[menor]:
                menor = k
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista