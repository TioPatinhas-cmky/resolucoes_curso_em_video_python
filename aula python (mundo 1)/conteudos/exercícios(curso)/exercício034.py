salário = float(input('qual é o salário do funcionário ?R$'))
base = 1250
aumento = salário + (salário*10/100)
if salário<= base:
    print('o funcionário que ganhava R${} passou a ganhar R${:.2f}'.format(salário, aumento))
else:
    print('o funcionário que ganhava R${} passou a ganhar R${:.2f}'.format(salário, aumento))