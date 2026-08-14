num = []

for i in range(0, 5):
    n = int(input(f"Digite o {i}° valor: "))
    num.append(n)

maior = max(num)
maiorPos = ""
menor = min(num)
menorPos = ""

for i, v in enumerate(num):
    print(f"{i}: {v}")
    if v == maior:
        maiorPos += f"{i}..."
    elif v == menor:
        menorPos += f"{i}..."

print(f"O maior valor digitado foi {maior}, nas posições {maiorPos}. \nO menor valor digitado foi {menor}, nas posições {menorPos}.")