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
    limite = 0
    for i in range(len(vector)): 
        limite += 1
        for j in range(limite, len(vector)):
            if vector[j] < vector[i]:    
                vector[j], vector[i] = vector[i], vector[j]