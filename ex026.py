frase = str(input('Digite uma frase: ')).strip().upper()  # lê a frase, remove espaços e coloca em maiúsculas
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))  # conta quantas vezes a letra A aparece
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))  # mostra a primeira posição da letra A
print('A última letra A aparece na posição {}'.format(frase.rfind('A') + 1))  # mostra a última posição da letra A