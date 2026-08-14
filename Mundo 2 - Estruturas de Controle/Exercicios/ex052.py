from datetime import date

atual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da {i}° pessoa : "))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1

print(f"Ao total temos {maior} {"pessoas maiores" if maior > 1 else "pessoa maior" } de idade \ne {menor} {"pessoas menores" if menor > 1 else "pessoa menor" } de idade")