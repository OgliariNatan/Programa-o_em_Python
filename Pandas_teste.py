import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('Inicio do código\n')
##############################################
def pessoa (nome, sobrenome, idade):
    print('Nome : ' + nome)
    print('Sobrnome : ' + sobrenome)
    print('Idade : ' + str(idade))

d = {'nome':'Natan', 'sobrenome':'Ogliari', 'idade':28} #dicionario
pessoa(**d)
##############################################


df_satelites = pd.read_csv('satelites\\satelites_operando_comercialmente.csv', sep=';')
df_satelites.drop_duplicates(inplace=True)
df_satelites.reset_index(drop=True, inplace=True)


print(df_satelites.info())
df_satelites.head()

print(df_satelites.index) #Imprimi os arqiuivos dos csv

###Trabalhando com gráficos

"""plt.figure(figsize=(5,3))
plt.tick_params(labelsize=12)
sns.countplot(date=df_satelites, x='Tipo de Direito')"""

df_satelites_brasileiros = df_satelites.loc[df_satelites['Tipo de Direito'] == 'Brasileiro']
df_satelites_banda = df_satelites.loc[df_satelites['Posição orbital'] == '98ºO']
#plt.plot(df_satelites_brasileiros, df_satelites_banda)
plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_brasileiros, x='Bandas do satélite')

import scrapy

#https://www.hashtagtreinamentos.com/webscraping-no-python




class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'nota': response.css('strong::text').get()
            }