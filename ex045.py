import  random

# EM VEZ DE f'texto {variavel}', USA VÍRGULA NO PRINT
# print("Olá", nome)  →  MAIS FACÍL DE ENTENDER NO INICIO

print('-=-' * 20)
print('JOKENPÔ')
print('-=-' * 20)
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogador = int(input('digite sua escolha: '))
computador = random.randint(1, 3)

# MOSTRA O QUE O COMPUTADOR ESCOLHEU
if computador == 1:
    print('Computador escolheu: PEDRA')
elif computador == 2:
    print('Computador escolheu: PAPEL')
else:
    print('Computador escolheu: TESOURA')

# VERIFICA O RESULTADO
if jogador == computador:
    print('EMPATE!')
elif (jogador == 1 and computador == 3) or \
    (jogador == 3 and computador == 2) or \
    (jogador == 2 and computador == 1):
    print('VOCÊ VENCEU!')
else:
    print('COMPUTADOR VENCEU!')

import random

print('-=-' * 20)
print('JOKENPÔ')
print('-=-' * 20)
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogador = int(input('Digite sua escolha: '))
computador = random.randint(1, 3)

#f-string: VARIÁVEL DERETO DENTRO DO {}
print(f'Você escolheu: {jogador}')

if computador == 1:
    nome_pc = 'PEDRA'
elif computador == 2:
    nome_pc = 'PAPEL'
else:
    nome_pc = 'TESOURA'

# PODE COLOCAR DUAS VARIÁVEIS NA MESMA LINHA
print(f'Você: {jogador} | computador: {nome_pc}')

if jogador == computador:
    print('EMPATE!')
elif (jogador == 1 and computador == 3) or \
     (jogador == 3 and computador == 2) or \
     (jogador == 2 and computador == 1):
    print('Você VENCEU!')
else:
    print('COMPUTADOR VENCEU!')


