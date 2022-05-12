print('='*10 + 'Desafio 08' + '='*10)

valor = float(input('\nValor em Metro: '))

mm = valor * 1000
cm = valor * 100
dm = valor * 10
dam = valor / 10
hm = valor / 100
km = valor / 1000


print(f'Valor: {valor}m\n\nMilímetro: {mm:.2f}mm\nCentrímetro: {cm:.2f}cm\nDecimetro: {dm}dm\nDecametro: {dam}dam\nHectometro: {hm}hm\nQuilômetro: {km}km')