from random import randint  # importa a função randint para gerar números aleatórios

computador = randint(0, 5)  # faz o computador pensar em um número entre 0 e 5
print('-=-' * 20)  # imprime uma linha decorativa
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')  # avisa o desafio ao jogador
print('-=-' * 20)  # imprime outra linha decorativa
jogador = int(input('Em que numero eu pensei? '))  # lê a tentativa do jogador
if jogador == computador:  # verifica se o jogador acertou
    print('PARABÉNS! Você conseguiu me vencer!')  # mensagem de vitória do jogador
else:  # caso o jogador erre
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))  # mostra o número correto

# OU COM O time import sleep

from random import randint  # importa a função randint para gerar números aleatórios
from time import sleep  # importa a função sleep para pausar o programa
computador = randint(0, 5)  # faz o computador pensar em um número entre 0 e 5
print('-=-' * 20)  # imprime uma linha decorativa
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')  # avisa o desafio ao jogador
print('-=-' * 20)  # imprime outra linha decorativa
jogador = int(input('Em que numero eu pensei? '))  # lê a tentativa do jogador
print('PROCESSANDO...')  # mostra que o programa está processando
sleep(2)  # espera 2 segundos
if jogador == computador:  # verifica se o jogador acertou
    print('PARABÉNS! Você conseguiu me vencer!')  # mensagem de vitória do jogador
else:  # caso o jogador erre
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(computador, jogador))  # mostra o número correto