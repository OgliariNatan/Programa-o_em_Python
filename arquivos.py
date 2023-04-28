#coding: utf-8

'''scripty para ler arquivos'''

#Para ler arquivos
with open("log.txt", 'r') as log:
    for linha in log:
        print(linha)

palavras = ['NAtan', 'teste', 'maluco', "python"]
#Para escrever arquivos
with open("log.txt",'a') as log_1:
    for palavra in palavras:
        log_1.write(palavra + '\n')

with open('log.txt', 'r') as log:
    for linha in log:
        print(linha)