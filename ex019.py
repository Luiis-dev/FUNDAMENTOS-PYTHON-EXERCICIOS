import random  # importa a biblioteca de aleatoriedade

n1 = str(input('Primeiro aluno: '))  # lê o nome do primeiro aluno
n2 = str(input('Segundo aluno: '))  # lê o nome do segundo aluno
n3 = str(input('Terceiro aluno: '))  # lê o nome do terceiro aluno
n4 = str(input('Quarto aluno: '))  # lê o nome do quarto aluno
lista = [n1, n2, n3, n4]  # cria uma lista com os nomes
escolhido = random.choice(lista)  # escolhe um nome aleatório da lista
print('O aluno escolhido foi {}'.format(escolhido))  # mostra o escolhido

# OU

from random import choice  # importa apenas a função choice

n1 = str(input('Primeiro aluno: '))  # lê o nome do primeiro aluno
n2 = str(input('Segundo aluno: '))  # lê o nome do segundo aluno
n3 = str(input('Terceiro aluno: '))  # lê o nome do terceiro aluno
n4 = str(input('Quarto aluno: '))  # lê o nome do quarto aluno
lista = [n1, n2, n3, n4]  # cria uma lista com os nomes
escolhido = choice(lista)  # escolhe um nome aleatório da lista
print('O aluno escolhido foi {}'.format(escolhido))  # mostra o escolhido