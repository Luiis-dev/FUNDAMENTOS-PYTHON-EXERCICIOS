dias = int(input('Quantos dias alugados? '))  # lê quantos dias o carro foi alugado
km = float(input('Quantos km rodados? '))  # lê quantos quilômetros foram rodados
pago = (dias * 60) + (km * 0.15)  # calcula o valor total a pagar
print('O total a pagar é de R${:.2f}'.format(pago))  # mostra o total formatado com 2 casas decimais