nome = input('Qual é o seu nome? ')  # lê o nome do usuário
print('prazer em te conhecer {:20}'.format(nome))  # exibe o nome alinhado em 20 espaços à direita

# ...

nome = input('Qual é o seu nome? ')  # lê o nome do usuário
print('prazer em te conhecer {:>20}'.format(nome))  # alinha o texto em 20 espaços à direita

# ...

nome = input('Qual é o seu nome? ')  # lê o nome do usuário
print('prazer em te conhecer {:<20}'.format(nome))  # alinha o texto em 20 espaços à esquerda

# ...

nome = input('Qual é o seu nome? ')  # lê o nome do usuário
print('prazer em te conhecer {:^20}'.format(nome))  # centraliza o texto em 20 espaços

# ...

nome = str(input('Qual é o seu nome? '))  # lê o nome como string
print('prazer em te conhecer {:=^20}'.format(nome))  # centraliza e preenche com "="

n1 = int(input('um valor: '))  # lê o primeiro número inteiro
n2 = int(input('um valor: '))  # lê o segundo número inteiro
print('A soma entre {}'.format(n1+n2))  # mostra a soma

# OU

n1 = int(input('um valor: '))  # lê o primeiro número inteiro
n2 = int(input('um valor: '))  # lê o segundo número inteiro
s = n1 + n2  # calcula a soma
m = n1 * n2  # calcula a multiplicação
d = n1 / n2  # calcula a divisão
di = n1 // n2  # calcula a divisão inteira
e = n1 ** n2  # calcula a potência
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))  # exibe soma, produto e divisão
print('Divisão inteira {} e potência {}'.format(di, e))  # exibe divisão inteira e potência

# COM CASAS DECIMAIS {:.?f}

n1 = int(input('um valor: '))  # lê o primeiro número inteiro
n2 = int(input('um valor: '))  # lê o segundo número inteiro
s = n1 + n2  # calcula a soma
m = n1 * n2  # calcula a multiplicação
d = n1 / n2  # calcula a divisão
di = n1 // n2  # calcula a divisão inteira
e = n1 ** n2  # calcula a potência
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))  # mostra a divisão com 3 casas decimais
print('Divisão inteira {} e potência {}'.format(di, e))  # exibe os outros resultados

# PARA NÃO QUEBRAR LINHA NO FINAL = end=' '

n1 = int(input('um valor: '))  # lê o primeiro número inteiro
n2 = int(input('um valor: '))  # lê o segundo número inteiro
s = n1 + n2  # calcula a soma
m = n1 * n2  # calcula a multiplicação
d = n1 / n2  # calcula a divisão
di = n1 // n2  # calcula a divisão inteira
e = n1 ** n2  # calcula a potência
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')  # mantém a próxima saída na mesma linha
print('Divisão inteira {} e potência {}'.format(di, e))  # continua a saída

# QUEBRA DE LINHA NO MEIO \n

n1 = int(input('um valor: '))  # lê o primeiro número inteiro
n2 = int(input('um valor: '))  # lê o segundo número inteiro
s = n1 + n2  # calcula a soma
m = n1 * n2  # calcula a multiplicação
d = n1 / n2  # calcula a divisão
di = n1 // n2  # calcula a divisão inteira
e = n1 ** n2  # calcula a potência
print('A soma é {},\n o produto é {} e a \n divisão é {}'.format(s, m, d), end=' >>> ')  # insere quebras de linha no texto
print('Divisão inteira {} e potência {}'.format(di, e))  # exibe a continuação