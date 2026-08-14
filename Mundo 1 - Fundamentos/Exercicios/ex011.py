salario = float(input("Digite o salário: R$ "))
aumento = float(input("Digite o aumento (em %): "))
novoSalario = salario * (1 + (aumento/100))
print(f"O funcionário que ganhava R$ {salario}, com aumento de {aumento}% irá receber R$ {novoSalario}")