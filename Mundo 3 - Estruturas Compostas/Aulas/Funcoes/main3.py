def contador(lista: list[int]):
    som = 0
    for L in lista:
        som += L
    print(f"Recebi {len(lista)} números, são eles: {lista}, \nao todo a soma deles é: {som}")

l = list()
count = int(input("Quantos valores quer digitar? "))

for i in range(0, count):
    n = int(input(f"{i+1}° valor: "))
    l.append(n)

contador(l)