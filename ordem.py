# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n - 1):  # Serão no máximo n-1 iterações
#         for j in range(n - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#         print(f"{i + 1} Iteração : {lista[:]}")  # Mostra a lista após cada iteração

# # Exemplo
# lista = [3, 7, 5, 2, 1]
# print("Lista original:", lista)
# bubble_sort(lista)
# print("Lista ordenada:", lista)


def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):  # Serão no máximo n-1 iterações
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
        print(f"{i + 1} Iteração : {lista[:]}")  # Mostra a lista após cada iteração

# Exemplo
lista = [9, 5, 1, 4, 3, 8, 2, 6, 7, 0]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)
