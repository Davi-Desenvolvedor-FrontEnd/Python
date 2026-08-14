import datetime

dados = {
    "nome": input("Nome: "),
    "ano": int(input("Ano de Nascimento: ")),
    "sexo": str(input("Sexo [M/F]: ")),
    "ctps": int(input("Carteira de Trabalho: "))
}

if dados["ctps"] != 0:
    dados["salario"] = float(input("Sálario: "))
    idade = datetime.datetime.now().year - dados["ano"]
    if dados["sexo"] in "Ff":
        dados["aposentadoria"] = idade + 30
    else:
        dados["aposentadoria"] = idade + 35

for k, v in dados.items():
    print(f"{k}: {v}")