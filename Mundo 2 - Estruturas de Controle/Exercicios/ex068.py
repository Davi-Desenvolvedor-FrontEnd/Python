print("-=" * 20)
print("CAIXA ELETRÔNICO")
print("-=" * 20)

dinheiro = int(input("Qual o valor do saque: R$ "))
celula50 = dinheiro // 50
celula20 = (dinheiro - (celula50 * 50))//20
celula10 = (dinheiro - (celula50 * 50) - (celula20 * 20))//10
celula1 = dinheiro - (celula50 * 50) - (celula20 * 20) - (celula10 * 10)

if celula50 > 0:
    print(f"Total de cédulas de R$ 50: {celula50}")
if celula20 > 0:
    print(f"Total de cédulas de R$ 20: {celula20}")
if celula10 > 0:
    print(f"Total de cédulas de R$ 10: {celula10}")
if celula1 > 0:
    print(f"Total de cédulas de R$ 1: {celula1}")

# ou

print("-=" * 20)
print("CAIXA ELETRÔNICO")
print("-=" * 20)

totCed = 0
ced = 50

dinheiro = int(input("Qual o valor do saque: R$ "))
total = dinheiro
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f"Total de cédulas de R$ {ced}: {totCed}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break