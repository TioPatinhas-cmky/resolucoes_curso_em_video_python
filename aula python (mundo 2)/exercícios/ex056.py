i = 0
maioridadehomem = 0 
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print(f'------{c}° PESSOA------')
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo? (M) (F) '))
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
i += idade
print(f'A média de idade entre as pessoas é {i/4}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'{totmulher20} mulheres são mais novas que 20 anos')
