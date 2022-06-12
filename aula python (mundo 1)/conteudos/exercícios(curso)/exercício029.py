v = int(input('qual é a velocidade atual ? '))
if v<=80:
    print('tenha um ótimo dia! dirija com segurança')
else:
    print('você foi multado em {} reais! EXESSO DE VELOCIDADE'.format((v-80)*7))