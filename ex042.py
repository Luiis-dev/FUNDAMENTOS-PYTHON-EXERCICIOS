print('-=-' * 20)  # imprime uma linha decorativa
print('ANALISADOR DE TRIANGULO')  # mostra o título
print('-=-' * 20)  # imprime outra linha decorativa

r1 = float(input('Primeiro valor: '))  # lê o primeiro lado
r2 = float(input('Segundo valor: '))  # lê o segundo lado
r3 = float(input('Terceiro valor: '))  # lê o terceiro lado

if r1 == r2 == r3:  # verifica se os três lados são iguais
    print('EQUILÁTERO')  # triângulo equilátero
elif r1 != r2 and r1 != r3 and r2 != r3:  # verifica se todos os lados são diferentes
    print('ESCALENO')  # triângulo escaleno
else:  # caso contrário
    print('ISÓSCELES')  # triângulo isósceles