real = float(input('Quanto dinheiro você tem na carteira? R$'))  # lê o valor em reais
dolar = real / 5.16  # converte reais para dólares usando a cotação informada
print('Com R$ você pode comprar US${:.2f}'.format(real, dolar))  # mostra o valor convertido

# EURO

real = float(input('Quanto dinheiro você tem na carteira? R$ '))  # lê o valor em reais
euro = real / 6.10  # converte reais para euros usando a cotação informada
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(real, euro))  # mostra o valor convertido