n = int(input('Digite um número:  '))  # lê um número inteiro
d = n * 2  # calcula o dobro
t = n * 3  # calcula o triplo
r = n ** (1/2)  # calcula a raiz quadrada
print('O dobro de {} vale {}'.format(n, d))  # mostra o dobro
print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {}.'.format(n, t, n, r))  # mostra triplo e raiz

# COM QUEBRA DE LINHA = \n

n = int(input('Digite um número:  '))  # lê um número inteiro
d = n * 2  # calcula o dobro
t = n * 3  # calcula o triplo
r = n ** (1/2)  # calcula a raiz quadrada
print('O dobro de {} vale {}'.format(n, d))  # mostra o dobro
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {}.'.format(n, t, n, r))  # usa quebra de linha

# FORMATAÇÃO DECIMAL = :.?f

n = int(input('Digite um número:  '))  # lê um número inteiro
d = n * 2  # calcula o dobro
t = n * 3  # calcula o triplo
r = n ** (1/2)  # calcula a raiz quadrada
print('O dobro de {} vale {}'.format(n, d))  # mostra o dobro
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))  # mostra a raiz com 2 casas decimais

# OU POSIBILIDADE

n = int(input('Digite um número:  '))  # lê um número inteiro
print('O dobro de {} vale {}'.format(n, (n*2)))  # calcula o dobro direto na saída
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))  # calcula tudo direto

# OU POSIBILIDADE USANDO O pow

n = int(input('Digite um número:  '))  # lê um número inteiro
print('O dobro de {} vale {}'.format(n, (n*2)))  # calcula o dobro direto na saída
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))  # usa pow para a raiz