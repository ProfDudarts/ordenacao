from typing import List, Dict

def bubble_sort_dicts(data: List[Dict[str, any]], key: str) -> List[Dict[str, any]]:
    """Ordena a lista de dicionários usando o Bubble Sort de acordo com a chave especificada."""
    n = len(data)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True
        if not swap:
            return data #top d++++++++++++++++
    return data

def selection_sort_dicts(data: List[Dict[str, any]], key: str) -> List[Dict[str, any]]:
    """Ordena a lista de dicionários usando o Selection Sort de acordo com a chave especificada."""
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][key] < data[min_index][key]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

def insertion_sort_dicts(data: List[Dict[str, any]], key: str) -> List[Dict[str, any]]:
    """Ordena a lista de dicionários usando o Insertion Sort de acordo com a chave especificada."""
    n = len(data)
    for i in range(1, n):
        key_item = data[i]
        j = i - 1
        while j >= 0 and data[j][key] > key_item[key]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
    return data

def quick_sort_dicts(data: List[Dict[str, any]], key: str) -> List[Dict[str, any]]:
    """Ordena a lista de dicionários usando o Quick Sort de acordo com a chave especificada."""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][key]
    left = [item for item in data if item[key] < pivot]
    middle = [item for item in data if item[key] == pivot]
    right = [item for item in data if item[key] > pivot]
    return quick_sort_dicts(left, key) + middle + quick_sort_dicts(right, key)
