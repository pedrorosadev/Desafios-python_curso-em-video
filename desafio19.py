from random import choice

print('='*10 + 'Desafio 19' + '='*10 + '\n')

aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º Aluno: ')


listaAlunos = [aluno1, aluno2, aluno3, aluno4]


print(f'\nAluno que apagará o quadro: {choice(listaAlunos)}')
