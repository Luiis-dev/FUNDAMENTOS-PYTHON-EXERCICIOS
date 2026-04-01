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

# EXEMPLO GUSTAVO

r1 = float(input('Primeiro valor: '))  # lê o primeiro segmento
r2 = float(input('Segundo valor: '))  # lê o segundo segmento
r3 = float(input('Terceiro valor: '))  # lê o terceiro segmento
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # verifica se os segmentos formam triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')  # informa que pode formar triângulo
    if r1 == r2 ==r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:  # caso não forme triângulo
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

# OU

r1 = float(input('Primeiro valor: '))  # lê o primeiro segmento
r2 = float(input('Segundo valor: '))  # lê o segundo segmento
r3 = float(input('Terceiro valor: '))  # lê o terceiro segmento
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # verifica se os segmentos formam triângulo
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')  # informa que pode formar triângulo
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    if r1 == r2 and r2 == r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:  # caso não forme triângulo
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')