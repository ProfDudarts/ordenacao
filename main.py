from lib.busca import carregar_palavras, comparar_buscas
from lib.ordenacao import bubble_sort_dicts, selection_sort_dicts, insertion_sort_dicts, quick_sort_dicts
clientes = [
    {"nome": "Alice", "idade": 28, "pontuacao_credito": 650, "renda_anual": 45000},
    {"nome": "Bob", "idade": 35, "pontuacao_credito": 700, "renda_anual": 52000},
    {"nome": "Carlinhos", "idade": 40, "pontuacao_credito": 800, "renda_anual": 60000},
    {"nome": "Diana", "idade": 23, "pontuacao_credito": 720, "renda_anual": 48000}, 
    {"nome": "Edward", "idade": 31, "pontuacao_credito": 690, "renda_anual": 51000}
]

# arquivo = 'strings01milhao.txt'
# palavras = carregar_palavras(arquivo)

# palavra_busca = 'zzzqa'
# comparar_buscas(palavras, palavra_busca)

print(quick_sort_dicts(key='idade', data=clientes))
