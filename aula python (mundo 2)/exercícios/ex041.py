from datetime import date 

ano = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Sua categoria é MIRIM')

elif idade <= 14:
    print('Sua categoria é INFANTIL')

elif idade <= 19:
    print('Sua categoria é JUNIOR')

elif idade <=20:
    print('Sua categoria é junior')

elif idade > 20:
    print('Sua categoria é MASTER')