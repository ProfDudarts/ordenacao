
def bubble_sort(lista: list) -> None:
    changed = False

    for i in range(len(lista) - 1):
        current = lista[i]
        _next = lista[i + 1]

        if current > _next:
            lista[i] = _next
            lista[i + 1] = current
            changed = True
    
    if changed:
        bubble_sort(lista)