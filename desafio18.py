from math import sin, cos, tan, radians

print('='*10 + 'Desafio 18' + '='*10+ '\n')


angulo = float(input('Ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nSeno: {seno:.2}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')