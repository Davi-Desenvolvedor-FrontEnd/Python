import math
n = int(input("Digite um número para calcular seu fatorial: "))

print(f"{n}! = ", end='')
# for i in range(n, 0, -1):
#     print(f"{i} {"x" if i != 1 else "="} {math.factorial(n) if i == 1 else ''}", end="")
c = n
while c > 0:
    print(f"{c} {"x" if c != 1 else "="} {math.factorial(n) if c == 1 else ''}", end="")
    c -= 1
