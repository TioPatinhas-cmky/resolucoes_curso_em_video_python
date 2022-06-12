casa = float(input('Qual é o valor do imóvel? '))
salário = float(input('Qual é o salário do comprador? '))
anos = int(input('Em quantos anos irá pagar as prestações? '))
prestação = casa / (anos *12)
porcentagem = salário

print(f'Para pagar uma casa de {casa} em {anos}', end=' ')
print(f'A prestação será de {prestação:.2f}')

if prestação <= porcentagem:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')