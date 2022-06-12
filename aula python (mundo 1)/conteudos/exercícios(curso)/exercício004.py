frase = input('Digite algo: ')
print(f'''O tipo primitivo desse valor é {type(frase)}
tem só espaços ? {frase.isspace()}
é alfabético? {frase.isalpha()}
é número? {frase.isnumeric()}
está em maiuscula? {frase.isupper()}''')