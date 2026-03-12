import math
num = float(input('Digite um valor:  '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num))) # math.trunc cortar o numero

#  OU

from math import trunc
num = float(input('Digite um valor:  '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))  # math.trunc cortar o numero

#  OU


num = float(input('Digite um valor:  '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))

