num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
# ou
print(f"{num} é {"par"if num % 2 == 0 else "ímpar"}")