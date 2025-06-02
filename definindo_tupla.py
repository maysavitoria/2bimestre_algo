numero = (5, 8, 12, 8, 7, 8, 3)
#definindo uma tupla, pra ser uma tupla sempre se usa parênteses
print("tupla original:", numero)

print("tamanho da tupla:", len(numero)) #sao 7 elementos mas como começa do 0, o tamanho é 6 
print("tupla ordenada:", sorted(numero))

print(numero[2]) #acessando o 3 elemento da tupla
print(numero[2:5]) #acessando do 3 ao 5 elemento da tupla (slicing), n mostra o ultimo elemento pedido
print(numero[-1]) #acessando o ultimo elemento da tupla 
print("quantas vezes o número 8 aparece na tupla:", numero.count(8)) #contando quantas vezes o número 8 aparece na tupla

print("posição do número 7 na tupla:", numero.index(7)) #mostrando a posição do número 7 na tupla

minimo_tupla = min(numero) #mostrando o menor número da tupla
print("menor número da tupla:", minimo_tupla)

maximo_tupla = max(numero) #mostrando o maior número da tupla
print("maior número da tupla:", maximo_tupla)

soma_tupla = sum(numero) #mostrando a soma dos números da tupla
print("soma dos números da tupla:", soma_tupla)

print("o número 4 está na tupla?", 4 in numero) #verificando se o número 8 está na tupla

numero2 = (15, 20)
#concatenando tuplas
numero3 = numero + numero2
print("tupla concatenada:", numero3)
#concatenando é juntando, ou seja, não altera a tupla original pois gera uma nova tupla

#duplicando
numero4 = numero * 2
