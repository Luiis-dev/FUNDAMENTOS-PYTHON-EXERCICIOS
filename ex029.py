velocidade = float(input('Qual é a velocidade do carro? '))  # lê a velocidade do carro
if velocidade > 80:  # verifica se passou do limite
    print('MULTADO! você excedeu o limite permitido que é de 80km/h')  # avisa sobre a multa
    multa = (velocidade - 80) * 7  # calcula o valor da multa
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))  # mostra o valor da multa
print('Tenha um bom dia! Dirija com segurança!')  # mensagem final