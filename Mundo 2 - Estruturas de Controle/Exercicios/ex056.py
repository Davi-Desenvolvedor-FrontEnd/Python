import random

aleatorio = random.randint(1, 10)
acertou = False
tentativas = 0

while not acertou:
    num = int(input("Digite um número inteiro de 1 a 10: "))
    tentativas += 1
    if num > aleatorio:
        print("É menor")
    elif num < aleatorio:
        print("É maior")
    else:
        acertou = True
        
print(f"Parábens!!! Você acertou \nnúmero de tentativas: {tentativas}")