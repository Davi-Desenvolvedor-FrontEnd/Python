frase = input("Digite uma frase qualquer: ").strip().lower()
# nova = "".join(reversed(frase))
# novo = frase[::-1]
# if novo == frase:
#     print("É um palindromo")
# else:
#     print("Não é um palindromo")

palavras = frase.split()
junto = ''.join(palavras)
reverso = ''
for i in range(junto.__len__()-1, -1, -1):
    reverso += junto[i]
if reverso == frase:
    print("É um palindromo")
else:
    print("Não é um palindromo")