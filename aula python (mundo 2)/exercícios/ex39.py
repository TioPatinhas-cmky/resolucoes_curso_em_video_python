from datetime import date 
atual = date.today().year
nascimento = int(input('Qual é o ano do seu nascimento? '))
idade = atual - nascimento

print(f'Quem nasceu no ano {nascimento} tem {idade} anos em {atual}')

if idade == 18:
    print('Você já pode se alistar na Força Nacional Brasileira')

elif idade < 18:
    print(f'Você ainda não tem idade para se alistar, ainda restam {18-idade} anos')

elif idade > 18:
    print(f'Você deveria ter se alistado a {idade - 18} anos')