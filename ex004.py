# sem o tipo primitivo

a = int(input('digite algo: '))
print('o tipo primitivo desse vale {}'.format(type(a)))

# OU

a = int(input('digite algo: '))
print('O tipo primitivo desse vale {}'.format(type(a)))
print('Só tem espaços? ', a.isspace())   # a.issopace() se tem espaços
print('É um número? ', a.isnumeric())  # a.isnumeric() se é um número
print('É alfabético? ', a.isalpha())  # a.isalpha() se é um alfabético
print('É alfanúmerico? ', a.isalnum()) # a.isalnum() se é um alfabético e número
print('Está em maiúsculas? ', a.isupper()) # a.isupper() se está em maiúsculas
print('Está em minúsculas? ', a.islower()) # a.islower() se está em minúscalas
print('Está capitalizada? ', a.istitle()) # a.istitle() se está com maiúsculas e minúscalas

# a. E OBJETO ELE TEM CARACTERÍSTICAS E REALIZA FUNCIONALIDADES. SENDO APRIBUTOS E MÉTODOS
# NO CASO COMO FOI USADO () E OS MÉTODOS, POIS TODO OBJETO STRING TEM ESSE MÉTODOS: isspace, isnumeric......
