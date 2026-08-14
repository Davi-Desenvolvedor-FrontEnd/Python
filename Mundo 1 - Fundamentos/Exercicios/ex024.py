frase = input("Digite uma frase: ").replace(" ","")
print(frase)
print(f"Na frase {frase}, a letra 'a' aparece {frase.lower().count('a')} vezes \n a primeira na posição {frase.lower().find('a')+1} e a última na posição {frase.lower().rfind('a')+1}")