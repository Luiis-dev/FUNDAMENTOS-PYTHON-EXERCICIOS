num = int(input('Informe um número:  '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

# USANDO A MATEMÁTICA

num = int(input('Informe um número:  '))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(U))
print('Dezena: {}'.format(D))
print('Centena: {}'.format(C))
print('Milhar: {}'.format(M))