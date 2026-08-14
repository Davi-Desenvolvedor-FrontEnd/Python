import tabulate

aluno = {
    "nome": input("Digite o nome do aluno: "),
    "média": float(input("Digite a média escolar do aluno: ")),
    "frequência": int(input("Digite a frequência do aluno: ")),
    "situação": ""
}

if aluno["média"] >= 6 and aluno["frequência"] > 75:
    aluno["situação"] = "aprovado"
elif aluno["média"] < 6 and aluno["frequência"] < 75:
    aluno["situação"] = "reprovado"
elif aluno["média"] < 6 or aluno["frequência"] < 75:
    aluno["situação"] = "recuperação"

# for i, a in aluno.items():
#     print(f"{i}: {a}")

print(tabulate.tabulate(aluno.items(), headers="keys", tablefmt="fancy_grid"))