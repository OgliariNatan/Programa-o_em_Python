import pandas as pd




#pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

df_titanic = pd.read_csv("titanic.csv")
print(df_titanic.info())
df_titanic.head()

df_titanic.drop_duplicates(keep='last', inplace=True) #remove linhas duplicadas

print("Altera os tipos de dados \n")
df_titanic['Sex'] = df_titanic['Sex'].str.upper() # Coloca todos da linha em MAISCULO

df_titanic['Age'] = df_titanic['Age'].astype(int) #altera para int64

print(df_titanic.info())
df_titanic.head(2)

df_titanic['n_relatives'] = df_titanic['Siblings/Spouses Aboard'] + df_titanic['Parents/Children Aboard']
df_titanic.head()
print(df_titanic) #imprime toda a tabela

print('Manipulação de dados:')

idade_min = df_titanic['Age'].min()
idade_max = df_titanic['Age'].max()

intervalos = [idade_min-1, 10, 18, 65, idade_max]
rotulos = ['criança', 'adolescente', 'adulto', 'idoso']

df_titanic['faixa_idade'] = pd.cut(x=df_titanic['Age'], bins=intervalos, labels=rotulos)

print(df_titanic.info())
df_titanic.head()
print(df_titanic)

class_exis = df_titanic['Pclass'].unique()
print(class_exis)

# Qual a quantidade de sobreviventes e não sobreviventes?

filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_nao_sobreviventes = df_titanic['Survived'] == 0

qtde_sobreviventes = df_titanic.loc[filtro_sobreviventes].shape[0]
qtde_nao_sobreviventes = df_titanic.loc[filtro_nao_sobreviventes].shape[0]

print('\n\nQuantidade de sobreviventes = ', qtde_sobreviventes)
print('Quantidade de não sobreviventes = ', qtde_nao_sobreviventes)

# Quantos idosos estavam a bordo e quantos sobreviveram?

filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_idoso = df_titanic['faixa_idade'] == 'idoso'

qtde_idosos = df_titanic.loc[filtro_idoso].shape[0]
qtde_idosos_sobreviventes = df_titanic.loc[(filtro_sobreviventes) & (filtro_idoso)].shape[0]

print('\n\nQuantidade de idosos a bordo = ', qtde_idosos)
print('Quantidade de idosos que sobreviveram = ', qtde_idosos_sobreviventes)

# Das pessoas que sobreviveram, qual a taxa de sobrevivência entre homens e mulheres?

filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_homem = df_titanic['Sex'] == 'male'
filtro_mulher = df_titanic['Sex'] != 'male'

qtde_homens_sobreviveram = df_titanic.loc[(filtro_sobreviventes) & (filtro_homem)].shape[0]
qtde_mulheres_sobreviveram = df_titanic.loc[(filtro_sobreviventes) & (filtro_mulher)].shape[0]

# Para calcular a taxa de sobreviventes, precisamos do valor total de sobreviventes
qtde_passageiros_sobreviveram = df_titanic[filtro_sobreviventes].shape[0]

taxa_homens = qtde_homens_sobreviveram * 100 / qtde_passageiros_sobreviveram
taxa_mulheres = qtde_mulheres_sobreviveram * 100 / qtde_passageiros_sobreviveram

print("\n\nA taxa de sobreviventes homens foi = ", taxa_homens)
print("A taxa de sobreviventes mulheres foi = ", taxa_mulheres)

# Qual foi o valor médio da passagem entre os que sobreviveram e os que não sobreviveram?

filtro_sobreviventes = df_titanic['Survived'] == 1
filtro_nao_sobreviventes = df_titanic['Survived'] == 0

valor_medio_sobreviventes = df_titanic.loc[filtro_sobreviventes, 'Fare'].mean()
valor_medio_nao_sobreviventes = df_titanic.loc[filtro_nao_sobreviventes, 'Fare'].mean()

print('\n\nValor médio das passagens dos que sobreviveram = ', valor_medio_sobreviventes)
print('Valor médio das passagens dos que não sobreviveram = ', valor_medio_nao_sobreviventes)

#Filtro de sobriviventes

import tensorflow

