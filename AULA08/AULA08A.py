import math
num = int(input('Digite um número:  '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# SEGUNDA FORMA DA BIBLIOTECA SENDO INDIVIDUAL

from math import sqrt
num = int(input('Digite um número:  '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# floor

from math import sqrt, floor
num = int(input('Digite um número:  '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# NÚMERO ALEATORIO

import random
num = random.random()
print(num)

# NÚMERO INTEIRO DE  1, 10

import random
num = random.randint(1, 10)
print(num)

import emoji
print(emoji.emojize("Python é incrível :snake:"))
# Saída: Python é incrível 🐍

