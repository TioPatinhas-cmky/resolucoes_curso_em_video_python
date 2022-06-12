from random import randint
from time import sleep
computador = randint(0, 5) #esse comando faz o computador "pensar"
print('-=-' * 20)
print('ESTOU PENSANDO, TENTE ADIVINHAR O NÚMERO DE 0 A 5...')
print('-=-' * 20)
jogador = int(input('em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você acertou, parabéns!! eu pensei no número {}'.format(computador))
else:
    print('você errou, eu não pensei no número {}, eu pensei no número {}'.format(jogador,computador))