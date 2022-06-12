import random
a1 = str(input('qual o nome do primeiro aluno ?'))
a2 = str(input('qual o nome do segundo aluno ?'))
a3 = str(input('qual o nome do terceiro aluno ?'))
a4 = str(input('qual o nome do quarto aluno ?'))
sorteio = [a1, a2, a3, a4]
random.shuffle(sorteio)
print('a ordem de alunos para apresentar o trabalho foi:')
print(sorteio)