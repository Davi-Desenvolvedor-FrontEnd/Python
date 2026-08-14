import math

catOp = float(input("Digite o valor do cateto oposto: "))
catAdj = float(input("Digite o valor do cateto adjacente: "))
# hipotenusa = math.sqrt(math.pow(catOp, 2) + math.pow(catAdj, 2))
# ou
hipotenusa = math.hypot(catOp, catAdj)
print(f"No triângulo onde os catetos são {catOp} e {catAdj}, a hipotenusa é {hipotenusa:.1f}")