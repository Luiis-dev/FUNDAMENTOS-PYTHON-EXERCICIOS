import random  # importa a biblioteca random

# EM VEZ DE f'texto {variavel}', USA VÍRGULA NO PRINT
# print("Olá", nome)  →  MAIS FÁCIL DE ENTENDER NO INÍCIO

print('-=-' * 20)  # imprime uma linha decorativa
print('JOKENPÔ')  # mostra o título do jogo
print('-=-' * 20)  # imprime outra linha decorativa
print('1 - Pedra')  # opção pedra
print('2 - Papel')  # opção papel
print('3 - Tesoura')  # opção tesoura

jogador = int(input('digite sua escolha: '))  # lê a escolha do jogador
computador = random.randint(1, 3)  # sorteia a escolha do computador

# MOSTRA O QUE O COMPUTADOR ESCOLHEU
if computador == 1:  # se o computador escolheu 1
    print('Computador escolheu: PEDRA')  # mostra pedra
elif computador == 2:  # se o computador escolheu 2
    print('Computador escolheu: PAPEL')  # mostra papel
else:  # caso seja 3
    print('Computador escolheu: TESOURA')  # mostra tesoura

# VERIFICA O RESULTADO
if jogador == computador:  # verifica empate
    print('EMPATE!')  # mostra empate
elif (jogador == 1 and computador == 3) or \
    (jogador == 3 and computador == 2) or \
    (jogador == 2 and computador == 1):  # verifica se o jogador venceu
    print('VOCÊ VENCEU!')  # mostra vitória do jogador
else:  # caso o computador vença
    print('COMPUTADOR VENCEU!')  # mostra vitória do computador

import random  # importa random novamente

print('-=-' * 20)  # imprime uma linha decorativa
print('JOKENPÔ')  # mostra o título do jogo
print('-=-' * 20)  # imprime outra linha decorativa
print('1 - Pedra')  # opção pedra
print('2 - Papel')  # opção papel
print('3 - Tesoura')  # opção tesoura

jogador = int(input('Digite sua escolha: '))  # lê a escolha do jogador
computador = random.randint(1, 3)  # sorteia a escolha do computador

# f-string: variável direto dentro do {}
print(f'Você escolheu: {jogador}')  # mostra a escolha do jogador

if computador == 1:  # se o computador escolheu 1
    nome_pc = 'PEDRA'  # define o nome da jogada
elif computador == 2:  # se o computador escolheu 2
    nome_pc = 'PAPEL'  # define o nome da jogada
else:  # caso seja 3
    nome_pc = 'TESOURA'  # define o nome da jogada

# PODE COLOCAR DUAS VARIÁVEIS NA MESMA LINHA
print(f'Você: {jogador} | computador: {nome_pc}')  # mostra ambas as escolhas

if jogador == computador:  # verifica empate
    print('EMPATE!')  # mostra empate
elif (jogador == 1 and computador == 3) or \
     (jogador == 3 and computador == 2) or \
     (jogador == 2 and computador == 1):  # verifica se o jogador venceu
    print('Você VENCEU!')  # mostra vitória do jogador
else:  # caso o computador vença
    print('COMPUTADOR VENCEU!')  # mostra vitória do computador