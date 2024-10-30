lista = [3, 0, 2, 5, 11, 9, 7]

def bubble_in(lista):
    qtd = len(lista)
    for i in range(qtd):
        for j in range(0, qtd - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocado = True

        if not trocado:
            break
    return lista

print(lista)
print(bubble_in(lista))