import inspect
import math


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

arq=open("C:\Users\AULA-1\Documents\(Engenharia de Software)\Fase 1\Linguagem de Programação\Programa-o_em_Python\log.txt","r")
conteudo = arq.read()
print(f"O conteudo de log.txt e: \n {conteudo}")
arq.close()