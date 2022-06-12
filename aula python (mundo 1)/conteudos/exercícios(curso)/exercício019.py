import random

a1 = input('nome do aluno 1:')
a2 = input('nome do aluno 2:')
a3 = input('nome do aluno 3:')
a4 = input('nome do aluno 4:')
sorteio = (a1, a2, a3, a4)
print('o aluno sorteado foi:', random.choice(sorteio))
