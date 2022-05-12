print('='*10 + 'Desafio 04' + '='*10)

mensagem = input('\nDigite algo: ')

print(f'\nÉ numérico: {mensagem.isnumeric()}\nÉ alfabético: {mensagem.isalpha()}\nÉ alfa-numérico: {mensagem.isalnum()}\nPossui espaço: {mensagem.isspace()}\nÉ tudo maiúsculo: {mensagem.isupper()}\nÉ tudo minúsculo: {mensagem.islower()}\nCapitalizado: {mensagem.capitalize()}\n')