import random

print('='*10 + 'Desafio 20' + '='*10 + '\n')

aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º Aluno: ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listaAlunos)

print(f'\nOrdem da Apresentação:\n{listaAlunos}')

