p1 = int(input('Digite um numero inteiro: '))  # lê o primeiro número inteiro
p2 = int(input('Digite outro numero inteiro: '))  # lê o segundo número inteiro

if p1 > p2:  # verifica se o primeiro é maior
    print('{} É maior que {}'.format(p1, p2))  # mostra que p1 é maior
elif p1 < p2:  # verifica se o primeiro é menor
    print('{} É menor que {}'.format(p1, p2))  # mostra que p1 é menor
else:  # caso sejam iguais
    print('Não existe valor, maior, os dois são iguais')  # informa que os dois números são iguais