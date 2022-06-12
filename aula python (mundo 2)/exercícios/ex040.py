pn = float(input('Qual é a primeira nota do aluno? '))
sn = float(input('Qial é a segunda nota do aluno? '))
m = (pn + sn) / 2

print(f'Tirando {pn} e {sn} a média do aluno vai ser {m}')

if m < 5:
    print('O aluno foi reprovado.')

elif 7 > m >= 5:
    print('O aluno está em recuperação.')

elif m > 7:
    print('O aluno está aprovado.')