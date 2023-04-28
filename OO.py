#coding: utf-8
from math import pi, e
import datetime

'''
    Para exercicio de orirntado a objetos
'''

print("Defenição de Classe")
class Cachorro:

    especie = "Canis lupus familiaris"
    reino = "Animalia"
    def __int__(self, nome, idade, raca, data=datetime.date.today()):
        self.nome = nome
        self.idade = idade
        self._raca = raca
        self.date = data

    def latir(self):
        print(f"au-au. Meu nome é: {self.nome}")
        print(f"Meu reino é: {Cachorro.reino}")
    def aumentar_idade (self, valor):
        self.idade += valor

meu_cachorro = Cachorro()


class Proprietario(Cachorro):
    def __int__(self, NomeProprietario, EnderecoPro):
        self.EnderecoPro = EnderecoPro
        self.NomeProprietario = NomeProprietario

dono_cachorro = Proprietario()

class Circulo:
    def __int__(self, raio=1):
        self.raio = raio

meu_circulo = Circulo()
meu_circulo.raio = e
print(f"O raio é {meu_circulo.raio}\n")


meu_cachorro.nome = "Toby"
meu_cachorro.idade = 10
meu_cachorro.raca = "Vira Lata"
meu_cachorro.date = datetime.date.today()
print(meu_cachorro.nome, meu_cachorro.idade, meu_cachorro.raca, meu_cachorro.date)

print("DEFINIÇÃO DE MÉTODOS")
print(f"O nome do meu cachorro é: {meu_cachorro.nome}\n A idade do meu cachorro é: {meu_cachorro.idade}\n Sua raça é: {meu_cachorro.raca}\n A data deste documento é: {meu_cachorro.date}")
print(meu_cachorro.latir())