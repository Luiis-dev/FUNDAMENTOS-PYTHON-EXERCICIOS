import math  # importa a biblioteca matemática

co = float(input('Digite o valor do cateto oposto: '))  # lê o cateto oposto
ca = float(input('Digite o valor do cateto adjacente: '))  # lê o cateto adjacente
hi = math.hypot(co, ca)  # calcula a hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))  # mostra o resultado com 2 casas decimais

#

from math import hypot  # importa apenas a função hypot

co = float(input('Digite o valor do cateto oposto: '))  # lê o cateto oposto
ca = float(input('Digite o valor do cateto adjacente: '))  # lê o cateto adjacente
hi = hypot(co, ca)  # calcula a hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))  # mostra o resultado com 2 casas decimais