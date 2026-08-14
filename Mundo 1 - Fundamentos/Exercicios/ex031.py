n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

print(f"O maior valor digitado foi: {max(n1, n2, n3)} \ne o menor valor digitado foi: {min(n1, n2, n3)}")
# ou
lista = [n1, n2, n3]
lista.sort()
print(lista)