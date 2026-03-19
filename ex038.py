p1 = int(input('Digite um numero inteiro: '))
p2 = int(input('Digite outro numero inteiro: '))
if p1 > p2:
    print('{} É maior que {}'.format(p1,p2))
elif p1 < p2:
    print('{} É menor que {}'.format(p1, p2))
else:
    print('Não existe valor, maior, os dois são iguais')
