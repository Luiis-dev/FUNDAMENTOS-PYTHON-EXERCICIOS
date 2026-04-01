print('-=-' * 20)  # imprime uma linha decorativa
print('Analisador de Triângulos')  # mostra o título do programa
print('-=-' * 20)  # imprime outra linha decorativa

r1 = float(input('Primeiro valor: '))  # lê o primeiro segmento
r2 = float(input('Segundo valor: '))  # lê o segundo segmento
r3 = float(input('Terceiro valor: '))  # lê o terceiro segmento

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # verifica se os segmentos formam triângulo
    print('Os segmentos acima PODEM FORMAR triângulos!')  # informa que pode formar triângulo
else:  # caso não forme triângulo
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')  # informa que não pode formar triângulo