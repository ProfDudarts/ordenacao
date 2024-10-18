
def bubble_sort(lista: list) -> None:
    tamanho = len(lista)

    for i in range(tamanho):
        verificador = False
        for j in range(tamanho-1):
            if lista[j] > lista[j+1]:
                verificador = True
                if verificador ==True:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                else:
                    pass