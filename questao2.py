# Autora: Ana Paula A. Arnold
# RU: 3805422
# Atividade Prática disciplina de Linguagem de programação
# Questão 2

# Imports para geração de números aleatórios e para plotagem do gráfico
import numpy as np
import matplotlib.pyplot as plt

a = 3 # 1° num RU
b = 8 # 2° num RU
c = 5 # 3° num é zero, substituído por 5

# Definição das cores dos pontos para o gráfico, cada ponto terá uma cor diferente
coresPontos = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'gray']

# Definindo "semente" para a criação dos números aletórios como 100
np.random.seed(100)

# Criando x como um array de tamanho 10, onde terá números inteiros aleatórios de 1 a 100
x = np.random.randint(1, 100, size=10)

# Definição da equação linear proposta no exercício
y = (a * x) + (b * x) - c

# Metódo scatter define que será um gráfico de dispersão, onde cada ponto será o resultado, definindo tambem as cores e a label para legenda
plt.scatter(x, y, c=coresPontos, label=f'Resultados equação linear y = ({a}x) + ({b}x) - {c}')
# Invocando método para exibir o eixo X
plt.xlabel('Eixo X')
# Invocando método para exibir o eixo Y
plt.ylabel('Eixo Y')
# Metódo responsável pela exibição da legenda
plt.legend()
# Método que exibe o gráfico criado na janela de plotagem
plt.show()
