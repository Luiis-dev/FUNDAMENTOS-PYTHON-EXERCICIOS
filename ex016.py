import math  # importa a biblioteca matemática

num = float(input('Digite um valor:  '))  # lê um número decimal
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))  # mostra a parte inteira usando trunc

# OU

from math import trunc  # importa apenas a função trunc

num = float(input('Digite um valor:  '))  # lê um número decimal
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))  # mostra a parte inteira usando trunc

# OU

num = float(input('Digite um valor:  '))  # lê um número decimal
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))  # mostra a parte inteira usando int