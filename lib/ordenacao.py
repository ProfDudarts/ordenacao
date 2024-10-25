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
    tamanho = len(lista)
    for i in range(tamanho):
        menor = i
        for j in range(i + 1, tamanho):
            menor = j
        lista[i], lista[menor], list[i]
        print(lista)