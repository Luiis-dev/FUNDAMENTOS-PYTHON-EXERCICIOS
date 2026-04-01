import math  # importa a biblioteca matemática

ângulo = float(input('Digite o Ângulo que você deseja: '))  # lê o valor do ângulo
seno = math.sin(math.radians(ângulo))  # converte para radianos e calcula o seno
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))  # mostra o seno com 2 casas decimais
cosseno = math.cos(math.radians(ângulo))  # converte para radianos e calcula o cosseno
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))  # mostra o cosseno com 2 casas decimais
tangente = math.tan(math.radians(ângulo))  # converte para radianos e calcula a tangente
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))  # mostra a tangente com 2 casas decimais

# OU

from math import radians, sin, cos, tan  # importa apenas as funções necessárias

ângulo = float(input('Digite o Ângulo que você deseja: '))  # lê o valor do ângulo
seno = sin(radians(ângulo))  # calcula o seno do ângulo em radianos
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))  # mostra o seno
cosseno = cos(radians(ângulo))  # calcula o cosseno do ângulo em radianos
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))  # mostra o cosseno
tangente = tan(radians(ângulo))  # calcula a tangente do ângulo em radianos
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))  # mostra a tangente