distância = float(input('Qual é a distância da sua viagem?  '))  # lê a distância da viagem
print('Você está prestes a começar uma viagem de {}km.'.format(distância))  # informa a distância
if distância <= 200:  # verifica se a viagem é curta
    preço = distância * 0.50  # calcula o preço por km para viagens curtas
else:  # caso a viagem seja longa
    preço = distância * 0.45  # calcula o preço por km para viagens longas
print('E o preço da sua passagem será de R${:.2f}'.format(preço))  # mostra o valor final

# OU SIMPLIFICADO

distância = float(input('Qual é a distância da sua viagem?  '))  # lê a distância da viagem
print('Você está prestes a começar uma viagem de {}km.'.format(distância))  # informa a distância
preço = distância * 0.50 if distância <= 200 else distância * 0.45  # calcula o preço com expressão condicional
print('E o preço da sua passagem será de R${:.2f}'.format(preço))  # mostra o valor final