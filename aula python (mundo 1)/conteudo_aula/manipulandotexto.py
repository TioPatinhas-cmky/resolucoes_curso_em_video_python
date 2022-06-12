#fatiamento de str


#localizar a letra onde está o número
frase = ('curso em vídeo Python'). strip()
print(frase[3])

#copiar até o número de caractéres desejado
print(frase[:14])

#de um caractére até o final
print(frase[9:])

#pegar um frase de um caractére até o outro caractére desejado
print(frase[5:9])

#começar de um valor x, pulando de x casa em x casa (contando o valor x de pular casas será ignorado)
print(frase[9:21:2])

#começar do caractére 0 e ir até o caractére desejado 
print(frase[:5])

#começar do caractére desejado e ir até o final da frase
print(frase[5:])

#começar da casa desejada, ir até o final pulando de x em x
print(frase[9::3])



#analise



#pedir o comprimento de uma frase
caractéres = len(frase)
print('a frase tem {} caractéres'.format(caractéres))



#pedir pra contar quantas letras (x) tem na frase
nl = frase.count('o')
print('a frase tem {} "o"'.format(nl))



#irá contar quantas letras (x) tem entre o caractére (x) ao (x)
nl2 = frase.count('o', 0, 14)
print('existem {} "o" do 0 ao 14'.format(nl2))



#contar quantas vezes encontrou uma palavra na frase 
np = frase.find('deo')
print('encontrei a palavra deo no caractére {}'.format(np))



#reverter palavra para outra desejada
print(frase.replace('Python', 'android'))



#deixar a frase em maiuscula 
fu = frase.upper()
print(fu)


#deixar a frase em minuscula 
fl = frase.lower()
print(fl)


#deixar frase somente com a primeira letra maiuscula
fp = frase.capitalize()
print(fp)


#deixar a frase com a primeira letra depois do espaço maiusculo 
ft = frase.title()
print(ft)



#para tirar espaços inúteis
frase2 = ('   Aprenda python  ')
fs = frase2.strip()
print(fs)


#para tirar espaços inúteis somente do lado desejado                R=Right=direita
frs = frase2.rstrip()
print(frs)



#para tirar espaços inúteis somente do lado desejado                L=Left=esquerda
fls = frase2.lstrip()
print(fls)


#divisão de string
fsp = frase.split()
print(fsp)

#para separar palavras e alterar o separador
print('-'.join(frase))


#para não contar os espaços na frase use:
print('a frase sem contar os espaços tem {} letras'.format(len(frase) - nome.count(' ')))