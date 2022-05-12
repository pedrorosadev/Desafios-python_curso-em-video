print('='*10 + 'Desafio 12' + '='*10)

preco = float(input('\nPreço R$ '))
desconto = preco * 5/100

print(f'Desconto: R${desconto:.2f}\nValor Final: R$ {preco - desconto:.2f}')