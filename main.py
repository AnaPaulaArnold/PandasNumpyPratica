# Autora: Ana Paula A. Arnold
# RU: 3805422
# Atividade Prática disciplina de Linguagem de programação
# Questão 1
import math

#Criação da classe Calculadora
class Calculadora:

    #Implementação do método de somar retornando o resultado
    def soma(self, num1, num2):
        return print(f'A soma de {num1} e {num2} é: {num1+num2} ')

    #Implementação do método de subtração retornando o resultado
    def subtracao(self, num1, num2):
        return print(f'A subtração de {num1} e {num2} é: {num1 - num2} ')

    #Implementação do método multiplicação retornando o resultado
    def multiplicao(self, num1, num2):
        return print(f'A multiplicação de {num1} e {num2} é: {num1 * num2} ')

    # Implementação do método divisão retornando o resultado
    def divisao(self, num1, num2):
        return print(f'A divisão de {num1} e {num2} é: {num1 / num2} ')

    # Implementação do método de exponenciação retornando o resultado
    def expoente(self, num1, num2):
        return print(f'O expoente de {num1} elevado à {num2} é: {pow(num1, num2)} ')

    # Implementação do método resto retornando como resultado o resto e seu quociente
    def resto(self, num1, num2):
        quociente, resto = divmod(num1, num2)
        return print(f'O resto da divisão de {num1} e {num2} é: {resto} sendo seu quociente {quociente} ')

    # Implementação do método raiz quadrada, onde é somado os dois números e retornando o resultado da raiz quadrada deles
    def raiz(self, num1, num2):
        return print(f'A soma de {num1} e {num2} é {num1 +num2} e a raiz quadrada da soma é: {math.sqrt(num1+num2)} ')


# Inicio, print Menu opções
print('Bem-vindo a sua Calculadora. \nPara selecionar, digite o número desejado:')

# Input para o usuário poder inserir a opção desejada de operação matemática, usando try/except para caso inserir um número não inteiro
try:
    opcao = int(input('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Expoente \n6 - Resto \n7 - Raiz quadrada da soma de dois números\n'))
except ValueError:
    print('O valor digitado não é válido.')
    opcao = int(input('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Expoente \n6 - Resto \n7 - Raiz quadrada da soma de dois números\n'))


# Instanciação da minha_calculadora
minha_calculadora = Calculadora()

# Input para o usuário poder inserir o primeiro número da conta matemática, mesma lógica com o try/except para caso ele inserir um número não inteiro
try:
    num1 = int(input('Digite um número inteiro: '))
except ValueError:
    print('O número digitado não é um inteiro')
    num1 = int(input('Digite um número inteiro: '))

# Input para o usuário poder inserir o segundo número da conta matemática, mesma lógica com o try/except para caso ele inserir um número não inteiro
try:
    num2 = int(input('Digite outro número inteiro: '))
except ValueError:
    print('O número digitado não é um inteiro')
    num2 = int(input('Digite outro número inteiro: '))

# Lógica de ifs para verificar a escolha realizada pelo usuário e chamar o método correspondente enviando os números inputados
if opcao == 1:
    minha_calculadora.soma(num1, num2)
elif opcao == 2:
    minha_calculadora.subtracao(num1, num2)
elif opcao == 3:
    minha_calculadora.multiplicao(num1, num2)
elif opcao == 4:
    minha_calculadora.divisao(num1, num2)
elif opcao == 5:
    minha_calculadora.expoente(num1, num2)
elif opcao == 6:
    minha_calculadora.resto(num1, num2)
elif opcao == 7:
    minha_calculadora.raiz(num1, num2)
else:
    print('Você digitou uma opção inválida')


