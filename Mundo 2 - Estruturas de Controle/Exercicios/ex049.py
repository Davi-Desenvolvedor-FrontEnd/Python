primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

for i in range(1, 11):
    termo = primeiroTermo + (i - 1)*razao
    print(f"{termo}, ", end="")