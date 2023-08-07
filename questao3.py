# Autora: Ana Paula A. Arnold
# RU: 3805422
# Atividade Prática disciplina de Linguagem de programação
# Questão 3

# Imports para a plotagem, geração de números e carregamento do csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o arquivo STORES.csv
df = pd.read_csv(r'C:\Users\anapa\Downloads\archive_stores\Stores.csv')

# Renomeando todas as colunas
df = df.rename(columns={
    'Store ID': 'Loja',
    'Store_Area': 'Area',
    'Items_Available': 'Itens',
    'Daily_Customer_Count': 'Visitantes',
    'Store_Sales': 'Vendas'
})

# Calculando valores Itens
itens = df[['Itens']].describe()
min_itens = itens.loc['min', 'Itens']
max_itens = itens.loc['max', 'Itens']
medio_itens = itens.loc['mean', 'Itens']
desvio_itens = itens.loc['std', 'Itens']

# Imprimindo na tela os valores calculados
print('\n-------- Valores de Itens --------')
print(f'Valor mínimo: {min_itens}')
print(f'Valor máximo: {max_itens}')
print(f'Valor médio: {medio_itens}')
print(f'Desvio padrão: {desvio_itens}')
print('--------------------------------\n')


# Calculando valores Visitantes
visitantes = df[['Visitantes']].describe()
min_visitantes = visitantes.loc['min', 'Visitantes']
max_visitantes = visitantes.loc['max', 'Visitantes']
medio_visitantes = visitantes.loc['mean', 'Visitantes']
desvio_visitantes = visitantes.loc['std', 'Visitantes']

# Imprimindo no terminal os valores calculados
print('\n-------- Valores de Visitantes --------')
print(f'Valor mínimo: {min_visitantes}')
print(f'Valor máximo: {max_visitantes}')
print(f'Valor médio: {medio_visitantes}')
print(f'Desvio padrão: {desvio_visitantes}')
print('--------------------------------\n')

# Calculando valores Vendas
vendas = df[['Vendas']].describe()
min_vendas = vendas.loc['min', 'Vendas']
max_vendas = vendas.loc['max', 'Vendas']
medio_vendas = vendas.loc['mean', 'Vendas']
desvio_vendas = vendas.loc['std', 'Vendas']

# Imprimindo no terminal os valores calculados
print('\n-------- Valores de Vendas --------')
print(f'Valor mínimo: {min_vendas}')
print(f'Valor máximo: {max_vendas}')
print(f'Valor médio: {medio_vendas}')
print(f'Desvio padrão: {desvio_vendas}')
print('--------------------------------\n')

# Criando os gráficos
plt.figure(figsize=(12, 4))
# Totalizando o tamanho total de pontos para geração das cores
total_pontos = len(df.index)
# Gerando cores
cores_pontos = np.random.rand(total_pontos)

#Gráfico 1: Itens
# Indicando posição do gráfico no plot
plt.subplot(1, 3, 1)
# Chamada para plotagem de gráfico de dispersão com paleta de cores tab10
plt.scatter(df.index, df['Itens'], c=cores_pontos, cmap='tab10', label='Itens')
# A seguir métodos para exibir os eixos
plt.xlabel('Lojas')
plt.ylabel('Itens')
# Método para exibir a legenda
plt.legend()

# Gráfico 2: Visitantes
# Indicando posição do gráfico no plot
plt.subplot(1, 3, 2)
# Chamada para plotagem de gráfico de dispersão com paleta de cores inferno
plt.scatter(df.index, df['Visitantes'], c=cores_pontos, cmap='inferno', label='Visitantes')
# A seguir métodos para exibir os eixos
plt.xlabel('Lojas')
plt.ylabel('Visitantes')
# Método para exibir a legenda
plt.legend()

# Gráfico 3: Vendas
# Indicando posição do gráfico no plot
plt.subplot(1, 3, 3)
# Chamada para plotagem de gráfico de dispersão com paleta de cores inferno
plt.scatter(df.index, df['Vendas'], c=cores_pontos, cmap='plasma', label='Vendas')
# A seguir métodos para exibir os eixos
plt.xlabel('Lojas')
plt.ylabel('Vendas')
# Método para exibir a legenda
plt.legend()

# Ajustando o layout dos subplots
plt.tight_layout()

# Método para exibir os gráficos
plt.show()


