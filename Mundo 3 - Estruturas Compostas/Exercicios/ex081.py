num = [[], []]

for i in range(0, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

for numeros in num:
    for numero in numeros:
        print(f"{numero}", end=" ")
print(f"\nonde são pares os valores: {sorted(num[0])} \ne ímpares os valores: {sorted(num[1])}")