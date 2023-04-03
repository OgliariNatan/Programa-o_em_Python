''''
    Codigos iniciais em python
    quase que uma salada de frutas.
'''
print("Olá Mundo") #Impressão simples na tela

#Impressões de string, letra por letra
minha_string = "NATAN"
print(minha_string[0])
print(minha_string[1])
print(minha_string[2])
print(minha_string[3])
print(minha_string[4])
print(" ")

#Divisão (slicing) de strings, imprime uma parcela da string
#<variável_string>[início:parada:passo], Passo poder ser negativo
print(minha_string[0:3:1])


#Impressoes por parametro
#f-strings
#print(f"Olá {nome}, seu sobrenome é: {sobrenome}"), O "f" não pode ter espaço
nome = "NATAN"
sobrenome = "OGLIARI"
print(f"Olá {nome}, seu sobrenome é: {sobrenome}")
print("")

"""Métodos de strings
    Strings têm métodos, que representam funcionalidades comuns que foram implementadas pelos desenvolvedores do Python, 
    para que possamos usá-las em nossos programas diretamente. Eles são muito úteis para realizarmos operações comuns.
    <variável_string>.<nome_do_método>(<argumentos>)
"""
print("Métodos de string")
print( f"A string é: {minha_string.capitalize()}") #imprime toda a string
print("Letras N"); print(minha_string.count("N")) #Conta quantas letras "X", possui na string
print(minha_string.find("N")) #Conta quantas letras iguais juntas possui
print(minha_string.index("T"))# Imprime a posição da letra Informada, se possuir duas imprime e primeira encontada
#Listas

minha_lista_letras = ["N","A","t","a","n"]
minha_lista_numero = [1,2,3,4,5]

minha_lista_aninhada = [1,2,3,4,5,6], ["a","o","p","b"]
print(minha_lista_letras[2]) #Imprime o caracter no index informado
print(minha_lista_aninhada[1]) #O index é para a lista em referencia

print(len(minha_lista_numero)) #Imprime o tamanho da lista

minha_lista_numero[0] = 10 #atualiza a posição da lista para novo valor

print("adicionar um valor ao final de uma lista com o método .append().")
minha_lista_numero.append(8)
print(minha_lista_numero)
print("remover um valor de uma lista com o método .remove()")
minha_lista_numero.remove(10)
print(minha_lista_numero)

#Tuplas
print("Tuplas usa-se o (), na lista usa-se o []")

minha_tuplas = (1, 2, 3, 4), ("A")
print(minha_tuplas)

#Dicionarios em pyhton
#chave:valor, chave1:valor1
meu_dic = {
    "a": 1, 2:"c", "?":"USUARIO INCORRETO"
}

print(len(meu_dic))
print(meu_dic["?"])
meu_dic["/"] = "Diretorio usual"
print(meu_dic["/"])

#Para excliur
# del meu_dic["c"]

print(minha_string)
size_minha_string = len(minha_string)
print(size_minha_string)
x=0
if size_minha_string >= 0:
     print(minha_string[x])
     --size_minha_string
     ++x
else:
    print(size_minha_string)
    print("FIM")