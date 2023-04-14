'''
    Algoritimos de buscas
'''
import requests
import pandas as pd
import basedosdados as bd
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

'''Função para ordenação de lista de ordem n'''

def ordenar_selecao(lista):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista_3 = [10, 9, 50, 100, 6, 45, 53, 65, 0, 12, 28, -3]

lista_impressao = ordenar_selecao(lista_3)

print('Lista Ordenada de ordem n: ',lista_impressao)


print( '\n--------------------------------\nOrdenação por BOLHA\n','-----------------------------\n')
def ordenar_bubbleShort (lista):
    n = len(lista)

    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista_4 = [12, 9, 55, 120, 6, 35, 55, 66, 0, 19, 25, -6]

lista_impressao = ordenar_bubbleShort(lista_4)
print('Lista ordenada pelo BUBBLE SHORT: ', lista_impressao, '\n')

print( '\n--------------------------------\nOrdenação por INSERÇÃO\n','-----------------------------\n')

def ordenacao_insercao(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i]
        j = i -1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j = j-1
        lista[j + 1] = valor_inserir
    return lista

lista_5 = [13, 8, 25, 130, 6, 35, 55, 77, 0, -9, 15, -6, 99]

lista_impressao = ordenacao_insercao(lista_5)

print('\n Lista por inserção: ', lista_impressao, '\n')

'''
df = bd.read_table(data_id='br-inep-ideb',
table_id = 'brasil',
billing_project_id = "busca")'''

#https://httpbin.org/forms/post
#http://voos.infraero.gov.br/hstvoos/RelatorioPortal.aspx
#https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

info = requests.get('https://httpbin.org/forms/post')
dados1 = info.text
#dados2 = info.json()
print(type(dados1))
#print(type(dados2))

dados = requests.get('https://alunodigitalead.unopar.br/ead_unopar')
dados3 = requests.status_codes

print(type(dados))

print(dados3)
#print(dados.json())
print('TESTANDO A CONEXÃO: ' + str(dados.status_code)) #Verifica a conexção
#print(dados.text) #Exibe o código fonte.
print(dados.headers)