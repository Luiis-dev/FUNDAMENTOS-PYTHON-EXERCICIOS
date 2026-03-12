larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {:2}x{:2} é sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parade, você precisará de {}l de tinta.'.format(tinta))
