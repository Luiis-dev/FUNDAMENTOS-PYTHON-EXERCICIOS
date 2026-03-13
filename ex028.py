from random import randint
computador = randint(0, 5) # faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))
#
#
#OU COM O time import sleep 
#
#
from random import randint
from time import sleep
computador = randint(0, 5)  # faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))
