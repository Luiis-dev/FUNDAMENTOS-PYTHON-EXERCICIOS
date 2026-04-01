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