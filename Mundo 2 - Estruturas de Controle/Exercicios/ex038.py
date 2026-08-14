from datetime import date
print("="*80)
print("Olá meu atleta, me informe seu ano de nascimento e te darei sua classificação.")
print("="*80)
ano = int(input())
idade = date.today().year - ano

if idade <= 9:
    cargo = "mirim"
elif idade <= 14:
    cargo = "infantil"
elif idade <= 19:
    cargo = "junior"
elif idade <= 25:
    cargo = "sênior"
else:
    cargo = "mestre"
print(f"O atleta tem {idade} anos e é {cargo}")