num = int(input("Digite um número inteiro para converter: "))
print("""Escolha uma base: 
[1] binária
[2] octal
[3] hexadecimal
""")
baseInt = int(input())

if baseInt == 1:
    numConvertido = bin(num)[2:]
    base = "binária"
elif baseInt == 2:
    numConvertido = oct(num)[2:]
    base = "octal"
else:
    numConvertido = hex(num)[2:]
    base = "hexadecimal"
print(f"O número {num} convertido para a base {base} é {numConvertido}")