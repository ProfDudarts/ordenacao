
def bubble_sort(lista: list) -> None:

    tamanho = len(lista) - 1
    contagem = 0
    for posicao in range(len(lista)):

        if posicao == tamanho:
            if contagem == 0:
                return lista
            else:
                bubble_sort(lista)

        elif lista[posicao] > lista[posicao + 1]:
            controle = lista[posicao]
            lista[posicao] = lista[posicao + 1]
            lista[posicao + 1] = controle
            contagem += 1
            continue
    return listinha
    

listinha = [3,0,1,8,7,2,9,4,6,5]
print(bubble_sort(listinha))
