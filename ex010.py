real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.16
print('Com R$ você pode comprar US${:.2f}'.format(real, dolar))

# EURO

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
euro = real / 6.10  # taxa atual: 1 euro ≈ R$ 6,10
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(real, euro))