número = int(input('Me diga número qualquer:  '))  # lê um número inteiro
resultado = número % 2  # calcula o resto da divisão por 2
if resultado == 0:  # verifica se o número é par
    print('O número {} é PAR'.format(resultado))  # mostra que é par
else:  # caso não seja par
    print('O número {} é IMPAR'.format(resultado))  # mostra que é ímpar