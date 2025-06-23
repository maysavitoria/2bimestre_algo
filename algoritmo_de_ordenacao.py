# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lista[j] > lista[j+1]:
#                 # Troca os elementos
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#     return lista

# lista = [1,3,5,7,8,0,2,4,6,9]
# ordenada = bubble_sort(lista)
# print(ordenada)

# def selection_sort(lista):
#     n = len(lista)

#     for i in range(n):
#         # Assume que o menor elemento está na posição atual
#         indice_menor = i

#         # Verifica o restante da lista
#         for j in range(i + 1, n):
#             if lista[j] < lista[indice_menor]:
#                 indice_menor = j

#         # Troca o menor elemento encontrado com o elemento da posição atual
#         lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

#     return lista

# # Exemplo de uso
# valores = [64, 25, 12, 22, 11, -23]
# print("Lista original:", valores)
# valores_ordenados = selection_sort(valores)
# print("Lista ordenada:", valores_ordenados)



