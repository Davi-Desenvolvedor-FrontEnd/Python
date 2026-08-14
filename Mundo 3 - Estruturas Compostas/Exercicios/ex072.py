from random import sample

numeros = ()

for i in range(1, 5):
    n = int(input(f"{i}° Valor: "))
    numeros += (n,)

count9 = numeros.count(9)
count3 = numeros.count(3)
print(numeros)
print(f"O número 9 apareceu {count9} {"vezes" if count9 != 1 else "vez"}")
print(f"O número 3 apareceu {count3} {"vezes" if count3 != 1 else "vez"}")
pares = ()
print("Valores pares digitados: ")
for n in numeros:
    if n % 2 == 0 and pares.count(n) == 0:
        pares += (n,)
        print(n, end=' ')
print("\n")
print("-"*40)