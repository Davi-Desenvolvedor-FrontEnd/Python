i=1
# while i <= 10:
#     print(i)
#     i+=1

pares = 0
impares = 0
while i <= 5:
    n = int(input("Digite um número: "))
    if n % 2 == 0 or n == 0:
        pares+=1
    else:
        impares+=1
    i+=1
print(f"Você digitou {pares} números pares e {impares} números impares.")