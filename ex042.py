print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 == r2 == r3:              # OU = if r1 and r2 and r3:
    print('EQUILÁTERO')
elif r1 != r2 and r1 != r3 and r2 != r3:          # OU = elif not(r1 == r2 or r1 == r3 or r2 == r3):
    print('ESCALENO')
else:
    print('ISÓSCELES')

