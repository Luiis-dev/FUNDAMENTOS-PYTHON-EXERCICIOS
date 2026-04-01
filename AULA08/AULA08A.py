import math  # importa a biblioteca matemática

num = int(input('Digite um número:  '))  # lê um número inteiro
raiz = math.sqrt(num)  # calcula a raiz quadrada
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))  # mostra o resultado com 2 casas decimais

# SEGUNDA FORMA DA BIBLIOTECA SENDO INDIVIDUAL

from math import sqrt  # importa apenas a função sqrt
num = int(input('Digite um número:  '))  # lê um número inteiro
raiz = sqrt(num)  # calcula a raiz quadrada
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))  # mostra o resultado formatado

# floor

from math import sqrt, floor  # importa sqrt e floor
num = int(input('Digite um número:  '))  # lê um número inteiro
raiz = sqrt(num)  # calcula a raiz quadrada
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))  # mostra a parte inteira da raiz

# NÚMERO ALEATÓRIO

import random  # importa a biblioteca de números aleatórios
num = random.random()  # gera um número decimal aleatório entre 0 e 1
print(num)  # exibe o número gerado

# NÚMERO INTEIRO DE 1 A 10

import random  # importa a biblioteca de números aleatórios
num = random.randint(1, 10)  # gera um número inteiro aleatório entre 1 e 10
print(num)  # exibe o número gerado

import emoji  # importa a biblioteca emoji
print(emoji.emojize("Python é incrível :snake:"))  # converte o código do emoji em símbolo
# Saída: Python é incrível 🐍