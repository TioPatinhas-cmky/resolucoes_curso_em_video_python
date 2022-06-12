pessoas_maiores = homens_cadastrados = mulheres_menores_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')

    print('-' * 20)
    idade = int(input('Qual é a idade da pessoa? '))
    sexo = str(input('Qual é o sexo da pessoa?[M/F] '))
    print('-' * 20)

    opção = str(input('Você quer continuar?[S/N] '))

    if opção in 'Nn':
        break

    if idade >= 18:
        pessoas_maiores += 1

    if idade < 20 and sexo in 'Ff':
        mulheres_menores_20 += 1
    
    if sexo in 'Mm':
        homens_cadastrados += 1
    
print(f'{pessoas_maiores} tem mais de 18 anos.\n{homens_cadastrados} homens foram cadastrados.\n{mulheres_menores_20} mulheres são menores que 20 anos.')