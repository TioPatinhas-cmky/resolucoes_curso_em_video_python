from random import randint
from time import sleep

jogadas = 0
computador = randint(0, 5)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Estou pensando em um número de 0 a 5...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

sleep(2)

jogador = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')

sleep(3)

if jogador == computador:
    print('Você acertou, PARABÉNS!!!')

else:
    while jogador != computador:
        jogadas += 1
        jogador = int(input('Você errou! Tente novamente: '))
        print('PROCESSANDO...')
        sleep(3)
        if jogador == computador:
            print('Você acertou, PARABÉNS!!!')
            
print(f'Você acertou com {jogadas +1} jogadas')
sleep(3)
