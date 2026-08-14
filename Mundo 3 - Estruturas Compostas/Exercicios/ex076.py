num = []

while True:
    n = int(input("Digite um valor: "))
    if n not in num:
        num.append(n)
    else:
        print("Valor duplicado, não vou adicionar.")
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    if continuar == "N":
        break

print("=-"*20)
num.sort()
print(num)
