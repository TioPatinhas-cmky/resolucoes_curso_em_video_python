primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
termo = primeiro
cont = 1
total = 0 
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}',end='->')
        termo += razao
        cont += 1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')