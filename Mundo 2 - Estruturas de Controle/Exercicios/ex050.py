num = int(input("Digite um número inteiro: "))
count = 0

for i in range(1, num + 1):
    # print(num, i, num % i)
    if num % i == 0:
        count += 1

if count == 2:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")