salário = float(input('Qual é o salário do funcionário? R$ '))  # lê o salário atual
if salário <= 1250:  # verifica se o salário é menor ou igual ao limite
    novo = salário + (salário * 15 / 100)  # calcula aumento de 15%
else:  # caso o salário seja maior que o limite
    novo = salário + (salário * 10 / 100)  # calcula aumento de 10%
print('Quem ganhava R$(:.2f) passe a ganhar R${:.2f} agora'.format(salário, novo))  # mostra o salário antigo e o novo