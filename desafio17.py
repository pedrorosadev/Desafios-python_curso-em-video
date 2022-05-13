from math import sqrt, pow

print('='*10 + 'Desafio 17' + '='*10)

catetoA = float(input('\nCateto A: '))
catetoB = float(input('Cateto B: '))
hipotenusa = sqrt(pow(catetoA, 2) + pow(catetoB, 2)) 

print(f'Hipotenusa: {hipotenusa:.2f}')