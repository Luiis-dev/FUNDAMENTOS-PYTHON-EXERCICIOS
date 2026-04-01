n = int(input('Digite um numero: '))  # lê um número inteiro informado pelo usuário
a = n - 1  # calcula o antecessor
s = n + 1  # calcula o sucessor
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))  # mostra o resultado

# SE EU PRECISAR DO ANTECESSOR E SUCESSOR MAIS PARA FRENTE O IDEAL É GUARDAR EM UMA VARIÁVEL
# SE FOR PARA MOSTRAR E PRONTO, PODE USAR ASSIM.

n = int(input('Digite um numero: '))  # lê um número inteiro informado pelo usuário
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))  # calcula direto na saída