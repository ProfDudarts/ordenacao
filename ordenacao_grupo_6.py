import json
import random
import string
import time

def gerar_dicionario():
    return {
        "id": random.randint(1, 10), 
        "nome": ''.join(random.choices(string.ascii_uppercase, k=5)),  
        "idade": random.randint(18, 99),  
        "cidade": ''.join(random.choices(string.ascii_uppercase, k=6)),  
    }

dados = [gerar_dicionario() for _ in range(100000)]
nome_arquivo = "Grupo_6.json"

with open(nome_arquivo, 'w') as f:
    json.dump(dados, f, indent=4)

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def selection_sort(arr, key):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i-1
        while j >= 0 and key_value[key] < arr[j][key]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_value
    return arr
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x[key] <= pivot[key]]
        greater = [x for x in arr[1:] if x[key] > pivot[key]]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)
def medir_tempo_execucao(algoritmo, dados, key):
    inicio = time.time()
    resultado = algoritmo(dados, key)
    fim = time.time()
    return fim - inicio

print("Lendo o arquivo JSON...")
with open("Grupo_6.json", 'r') as file:
    grupo_6 = json.load(file)

print("Iniciando ordenação por id com Bubble Sort...")
dados_ordenados_id = bubble_sort(grupo_6.copy(),"id")

print("\nIniciando ordenação por nome com Selection Sort...")
dados_ordenados_nome = selection_sort(grupo_6.copy(),"nome")

print("\nIniciando ordenação por idade com Insertion Sort...")
dados_ordenados_idade = insertion_sort(grupo_6.copy(),"idade")

print("\nIniciando ordenação por cidade com Quick Sort...")
dados_ordenados_cidade = quick_sort(grupo_6.copy(),"cidade")

dados_bubble = dados.copy()
dados_selection = dados.copy()
dados_insertion = dados.copy()
dados_quick = dados.copy()

tempo_bubble = medir_tempo_execucao(bubble_sort, dados_bubble, "id")
tempo_selection = medir_tempo_execucao(selection_sort, dados_selection, "id")
tempo_insertion = medir_tempo_execucao(insertion_sort, dados_insertion, "id")
tempo_quick = medir_tempo_execucao(quick_sort, dados_quick, "id")

print(f"\nTempo de execução Bubble Sort: {tempo_bubble:.4f} segundos")
print("Ordenado por id (primeiros 5):", dados_ordenados_id[:5])
print(f"\nTempo de execução Selection Sort: {tempo_selection:.4f} segundos")
print("Ordenado por nome (primeiros 5):", dados_ordenados_nome[:5])
print(f"\nTempo de execução Insertion Sort: {tempo_insertion:.4f} segundos")
print("Ordenado por idade (primeiros 5):", dados_ordenados_idade[:5])
print(f"\nTempo de execução Quick Sort: {tempo_quick:.4f} segundos")
print("Ordenado por cidade (primeiros 5):", dados_ordenados_cidade[:5])