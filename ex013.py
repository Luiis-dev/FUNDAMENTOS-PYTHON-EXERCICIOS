salário = float(input('Qual é o salário do Funcionário? R$'))  # lê o salário atual
novo = salário + (salário * 15 / 100)  # calcula o salário com aumento de 15%
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))  # mostra o novo salário