num = []
pares = []
impares = []

for i in range(0, 5):
    n = int(input("Digite um valor: "))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Os valores digitados foram: {num} \nnos quais os valores pares são: {pares} \ne os ímpares são: {impares}")