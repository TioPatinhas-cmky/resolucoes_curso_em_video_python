from random import choice
from time import sleep

print('''\033[32mSuas Opções:\033m
\033[33m[1]PEDRA
[2]PAPEL
[3]TESOURA\033[m''')

opção = int(input('Qual é a sua opção? '))
sleep(0.5)

print('JO')

sleep(0.5)

print('KEN')

sleep(0.5)

print('PO!!!')

sorteio = ('Pedra', 'Papel', 'Tesoura')
computador = choice(sorteio)

print(f'\033[31mComputador Jogou {computador}\033[m')

if opção == 3:
    if computador == 'Papel':
        print('\033[35mCOMPUTADOR PERDEU\033[m')
    elif computador == 'Pedra':
        print('\033[35mJOGADOR PERDEU\033[m')
    elif computador == 'Tesoura':
        print('\033[35mEMPATE\033[m')

if opção == 2:
    if computador == 'Pedra':
        print('\033[35mCOMPUTADOR PERDEU')
    elif computador == 'Papel':
        print('\033[35mEMPATE\033[m')
    elif computador == 'Tesoura':
        print('\033[35mJOGADOR PERDEU')

if opção == 1:
    if computador == 'Papel':
        print('\033[35mJOGADOR PERDEU')
    elif computador == 'Pedra':
        print('\033[35mEMPATE\033[m')
    elif computador == 'Tesoura':
        print('\033[35mCOMPUTADOR PERDEU\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')