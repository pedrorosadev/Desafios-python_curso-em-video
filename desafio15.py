print('='*10 + 'Desafio 15' + '='*10)

km = float(input('Qtd. Quilômetro Rodado: '))
diaria = int(input('Qtd. de dias com o veículo alugado: '))

valorTotal = diaria * 60 + 0.15 * km

print(f'Valor Total a Pagar: R$ {valorTotal:.2f}')