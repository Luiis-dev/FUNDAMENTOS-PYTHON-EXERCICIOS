preço = float(input('Qual é o preço do produto? R$ '))  # lê o preço original do produto
novo = preço - (preço * 5 / 100)  # calcula o preço com desconto de 5%
print('O produto que custava R${:.2f}, na promoção como desconto de 5% vai custar R${:.2}'.format(preço, novo))  # mostra o valor final