# sem o tipo primitivo

a = int(input('digite algo: '))  # lê o valor e converte para inteiro
print('o tipo primitivo desse vale {}'.format(type(a)))  # mostra o tipo da variável

# OU

a = int(input('digite algo: '))  # lê o valor e converte para inteiro
print('O tipo primitivo desse vale {}'.format(type(a)))  # mostra o tipo da variável
print('Só tem espaços? ', a.isspace())   # verifica se há apenas espaços
print('É um número? ', a.isnumeric())  # verifica se é numérico
print('É alfabético? ', a.isalpha())  # verifica se é formado apenas por letras
print('É alfanúmerico? ', a.isalnum()) # verifica se é alfabético ou numérico
print('Está em maiúsculas? ', a.isupper()) # verifica se está em maiúsculas
print('Está em minúsculas? ', a.islower()) # verifica se está em minúsculas
print('Está capitalizada? ', a.istitle()) # verifica se está capitalizada

# a. E OBJETO ELE TEM CARACTERÍSTICAS E REALIZA FUNCIONALIDADES. SENDO ATRIBUTOS E MÉTODOS
# NO CASO COMO FOI USADO () E OS MÉTODOS, POIS TODO OBJETO STRING TEM ESSES MÉTODOS: isspace, isnumeric......