salario = float(input("Digite o seu salario: "))

if salario <= 1250:
    salarioFinal = salario*1.15
else:
    salarioFinal = salario*1.1
print(f"Seu salário que antes era R$ {salario:.2f}, agora será R$ {salarioFinal:.2f}")