num = int(input('Informe um número:  '))  # lê um número inteiro
n = str(num)  # converte o número para string para acessar os dígitos
print('Analisando o número {}'.format(num))  # mostra o número informado
print('Unidade: {}'.format(n[3]))  # mostra a unidade
print('Dezena: {}'.format(n[2]))  # mostra a dezena
print('Centena: {}'.format(n[1]))  # mostra a centena
print('Milhar: {}'.format(n[0]))  # mostra o milhar

# USANDO A MATEMÁTICA

num = int(input('Informe um número:  '))  # lê um número inteiro
U = num // 1 % 10  # calcula o dígito da unidade
D = num // 10 % 10  # calcula o dígito da dezena
C = num // 100 % 10  # calcula o dígito da centena
M = num // 1000 % 10  # calcula o dígito do milhar
print('Analisando o número {}'.format(num))  # mostra o número informado
print('Unidade: {}'.format(U))  # mostra a unidade
print('Dezena: {}'.format(D))  # mostra a dezena
print('Centena: {}'.format(C))  # mostra a centena
print('Milhar: {}'.format(M))  # mostra o milhar