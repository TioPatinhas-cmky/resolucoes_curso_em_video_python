salário = float(input('qual é o valor do salário ?R$ '))
novo = salário + (salário * 15 / 100)
print('o funcionário recebia R${}, ele passou a receber R${:.2f} com o aumento de 15%'.format(salário, novo))