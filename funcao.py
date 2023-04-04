import inspect
import math
import os

'''
    Usado para exercitar funções
'''


def impressao(nome, sobrenome = "NADA INFORMADO"):
    print(f"Olá {nome}, seu sobrenome é: {sobrenome}")
    return "Sucesso"





minha_string = "NATAN"

nome = "NATAN"
sobrenome = "OGLIARI"

verificação = impressao(nome, sobrenome)

print(verificação)



'''Ler arquivos '''

with open("C:\Users\AULA-1\Documents\(Engenharia de Software)\Fase 1\Linguagem de Programação\Programa-o_em_Pythonlog.txt", "r") as arq:
    for linha in arq:
        print(linha)

'''Escrever arquivos'''

palavras = ["Código", "Python", "Verde", "Incrível"]

with open("C:/Users/AULA-1/Documents/(Engenharia de Software)/Fase 1/Linguagem\ de\ Programação/Programa-o_em_Python/ logcv.txt", "w+") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")