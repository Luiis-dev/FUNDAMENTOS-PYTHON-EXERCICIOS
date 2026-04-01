peso = float(input('Digite o seu peso: '))  # lê o peso da pessoa
altura = float(input('Digite sua altura: '))  # lê a altura da pessoa
imc = peso / (altura ** 2)  # calcula o IMC

if imc < 18.5:  # verifica se está abaixo do peso
    print('Abaixo do peso')  # mostra a classificação
elif imc < 25:  # verifica se está no peso ideal
    print('peso ideal')  # mostra a classificação
elif imc < 30:  # verifica se está com sobrepeso
    print('Sobrepeso')  # mostra a classificação
elif imc < 40:  # verifica se está com obesidade
    print('Obesidade')  # mostra a classificação
else:  # caso seja maior ou igual a 40
    print('Obesidade Mórbida')  # mostra a classificação

# EXEMPLO GUSTAVO

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

# OU

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc >= 18.5 and imc < 30:
    print('Você está em SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
