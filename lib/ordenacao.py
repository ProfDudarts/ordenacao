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

lista = [5,3,4,2,1]

def selection_sort(lista):
    
    for i in range(len(lista)):

        min_index = i
        
        for j in range(i +1, len(lista)):

            if lista[j] < lista[min_index]:

                min_index = j
        
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista



print(selection_sort(lista))