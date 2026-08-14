from _pydatetime import date
anoNasc = int(input("Diga o ano de nascimento: "))
idade = date.today().year - anoNasc

if idade < 18:
    saldo = 18 - idade
    print(f"Você tem {idade} anos e falta {saldo} {"anos" if saldo > 1 else "ano"} para o alistamento")
elif idade > 18:
    saldo = idade - 18
    print(f"Você tem {idade} anos e se alistou há {saldo} {"anos" if saldo > 1 else "ano"}")
else:
    print("Você tem 18 anos e já pode se alistar")