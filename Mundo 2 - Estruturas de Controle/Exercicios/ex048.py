print("Digite 6 números inteiros: \n")
soma = 0

for i in range(1, 7):
    num = int(input())
    if num % 2 == 0:
        soma += num

print(soma)