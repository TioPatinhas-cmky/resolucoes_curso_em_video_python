from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR:[P/I] ')).strip().upper() [0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. O total é de {total}')
    print('DEU PAR' if jogador % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1

        else:
            print('Você perdeu!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1

        else:
            print('Você perdeu!')
            break

    print('Vamos Jogar novamente...')
    
print(f'GAME OVER !!! Você venceu {v} vezes')