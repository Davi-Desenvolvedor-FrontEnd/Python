from random import randint

print("-="*20)
numeros = ()
count = 5
while count > 0:
    i = randint(1, 100)
    if i not in numeros and i > 0:
        numeros += (i,)
        count -= 1
print(numeros)
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
print("-="*20)