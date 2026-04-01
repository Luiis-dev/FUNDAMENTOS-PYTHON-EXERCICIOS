import random  # importa a biblioteca de aleatoriedade

n1 = str(input('Primeiro aluno: '))  # lê o nome do primeiro aluno
n2 = str(input('Segundo aluno: '))  # lê o nome do segundo aluno
n3 = str(input('Terceiro aluno: '))  # lê o nome do terceiro aluno
n4 = str(input('Quarto aluno: '))  # lê o nome do quarto aluno
lista = [n1, n2, n3, n4]  # cria uma lista com os alunos
random.shuffle(lista)  # embaralha a ordem da lista
print('A ordem de apresentação será {} ')  # mostra a frase da apresentação
print(lista)  # exibe a lista embaralhada

# OU

from random import shuffle  # importa apenas a função shuffle

n1 = str(input('Primeiro aluno: '))  # lê o nome do primeiro aluno
n2 = str(input('Segundo aluno: '))  # lê o nome do segundo aluno
n3 = str(input('Terceiro aluno: '))  # lê o nome do terceiro aluno
n4 = str(input('Quarto aluno: '))  # lê o nome do quarto aluno
lista = [n1, n2, n3, n4]  # cria uma lista com os alunos
shuffle(lista)  # embaralha a ordem da lista
print('A ordem de apresentação será {} ')  # mostra a frase da apresentação
print(lista)  # exibe a lista embaralhada