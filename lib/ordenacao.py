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

def selection_sort(lista):
    ordenacao = len(lista)  
    for i in range(ordenacao): 
        menor_indice = i  

    
        for j in range(i + 1, ordenacao):
            if lista[j] < lista[menor_indice]:  
                menor_indice = j  

        
        if menor_indice != i:
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    
    return lista

lista = [7, 9, 6, 5, 8, 4, 3, 2, 1, 10]
print(selection_sort(lista))

