nome = input('Qual é o seu nome? ')
print('prazer em te conhecer {:20}'.format(nome))  # {:20} A LINHAMENTOS
#
#
#
nome = input('Qual é o seu nome? ')
print('prazer em te conhecer {:>20}'.format(nome))  # {:>20} A LINHAMENTO EM 20 ESPAÇOS A DIREITA
#
#
#
nome = input('Qual é o seu nome? ')
print('prazer em te conhecer {:<20}'.format(nome))  # {:<20} A LINHAMENTO EM 20 ESPAÇOS A ESQUERDA
#
#
#
nome = input('Qual é o seu nome? ')
print('prazer em te conhecer {:<20}'.format(nome))  # {:^20} CENTRALIZADO EM 20 ESPAÇOS
#
#
#
nome = str(input('Qual é o seu nome? '))
print('prazer em te conhecer {:=^20}'.format(nome))  # {:=^20} NOME CENTRALIZADO EM 20 ESPAÇOS DE =




n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
print('A soma entre {}'.format(n1+n2))

# OU

n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o  produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

# COM CASAS DECIMAIS {:.?f}

n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o  produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

# PARA NÃO  QUEBRA DE LINHAS NO FINAL= , end=' '

n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o  produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

# QUEBRA DE LINHA NO MEIO \n

n1 = int(input('um valor: '))
n2 = int(input('um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o  produto é {} e a \n divisão é {}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))














