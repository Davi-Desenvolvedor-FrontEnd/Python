import math

def linha():
    print("-"*100)

linha()
print("Hello, World!")
linha()

def potencia(a, b):
    return int(math.pow(a, b))

x = int(input("Digite um número: "))
n = int(input("Digite sua potência: "))

print(potencia(x, n))