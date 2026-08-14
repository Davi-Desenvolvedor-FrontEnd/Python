nome = input("Digite seu nome: ")
nomeSeparado = nome.split()
firstNome = nomeSeparado[0]
lastNome = nomeSeparado[nomeSeparado.__len__()-1]
print(f"Olá {nome}, seu primeiro nome é {firstNome} e seu último nome é {lastNome}")