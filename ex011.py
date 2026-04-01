larg = float(input('Qual a largura da parede? '))  # lê a largura da parede
alt = float(input('Qual a altura da parede? '))  # lê a altura da parede
area = larg * alt  # calcula a área da parede
tinta = area / 2  # calcula quantos litros de tinta são necessários
print('Sua parede tem a dimensão de {:2}x{:2} é sua área é de {}m².'.format(larg, alt, area))  # mostra largura, altura e área
print('Para pintar essa parade, você precisará de {}l de tinta.'.format(tinta))  # mostra a quantidade de tinta