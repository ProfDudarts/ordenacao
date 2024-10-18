
def bubble_sort(lista: list) -> None:
    def sort(vector: list) -> list:
        def compare(a: float, b: float):
            if a > b:
                return b, a 
            return a, b
        
        for i in range(len(vector)-1):
            vector[i],vector[i+1] = compare(vector[i],vector[i+1])
        
        vector_len = len(vector)
        
        if vector_len <= 2:
            return vector
        return sort(vector[:vector_len-1])+ (vector[vector_len-1:])
    
    lista = sort(lista)


#  Guilherme P. Santos