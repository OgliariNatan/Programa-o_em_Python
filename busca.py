'''
    Algoritimos de buscas
'''

lista = [10, 4, 15, -3]
print('Lista não ordenada: ',lista)

lista_ordenada1 = sorted(lista) #Ordena a lista pelo metodo SORTED
lista_ordenada2 = lista.sort()

print('Lista ordenada = ', lista, '\n')
print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)

print('Realizou a ordenação por seleção de forma interna no Python\n')

lista_1 = [7, 4]
print('lista_1, não ordenada: ',lista_1)

if lista_1[0] > lista_1[1]:
    aux = lista_1[1]
    lista_1[1] = lista_1[0]
    lista_1[0] = aux
print('Lista_1 ordenada manualmente é:', lista_1, '\n')
print('\n\n Outra forma de ordenar é:')
lista_2 = [15, -5]
print('lista_2: ',lista_2)

if lista_2[0] > lista_2[1]:
    lista_2[0], lista_2[1] = lista_2[1], lista_2[0]
print('\nLista ordenada de forma mágica: ', lista_2, '\n')

