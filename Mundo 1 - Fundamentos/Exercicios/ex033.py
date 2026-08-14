print("="*25)
print("Analisador de Triângulos")
print("="*25)
lado1 = int(input("Digite o primeiro valor: "))
lado2 = int(input("Digite o segundo valor: "))
lado3 = int(input("Digite o terceiro valor: "))

if lado1 > (abs(lado2 - lado3)) and lado1 < (lado2+lado3):
    pode = True
if lado2 > (abs(lado1 - lado3)) and lado2 < (lado1 + lado3):
    pode = True
if lado3 > (abs(lado2 - lado1)) and lado3 < (lado2 + lado1):
    pode = True
else:
    pode = False
if pode:
    print("Pode ser triângulo!")
else:
    print("Não pode ser triângulo!")

arquivo = open("resultado.txt", "w")
arquivo.write(str(pode) + "\n")
arquivo.write(str(lado1) + "\n")
arquivo.write(str(lado2) + "\n")
arquivo.write(str(lado3) + "\n")
arquivo.close()