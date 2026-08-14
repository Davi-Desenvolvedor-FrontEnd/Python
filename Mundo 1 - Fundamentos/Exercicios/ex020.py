nome = input("Digite seu nome: ")
nomeLen = nome.replace(" ", "").__len__()
nomeLow = nome.lower()
nomeUpper = nome.upper()
nomeFirst = nome.split()[0]
nomeFirstLen = nomeFirst.__len__()
print(f"Analisando seu nome... \n seu nome tem {nomeLen} letras \n em maiúsculo é {nomeUpper} \n em minúsculo é {nomeLow} \n seu primeiro nome é {nomeFirst} e tem {nomeFirstLen} letras")