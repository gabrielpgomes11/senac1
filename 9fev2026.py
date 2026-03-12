#9/2/2026
faturamento=50000
percentualBonus=0.1
bonusTotal=faturamento*percentualBonus
faturamentoLiquido=faturamento-bonusTotal
print("Faturamento bruto: R$", f"{faturamento:,.2f}")
print("Bonus total: R$", f"{bonusTotal:,.2f}")
print("Faturamento líquido: R$", f"{faturamentoLiquido:,.2f}")

estoque = 250
vendas = 78
reposicao = 100
estoque = estoque - vendas + reposicao
print("Estoque atual:", estoque)

qtdCaixas = 1250
capacidadeCaminhao = 12
caminhoesCompletos = (qtdCaixas // capacidadeCaminhao)
print("Caminhões completos:", caminhoesCompletos)
restoCaixas = (qtdCaixas % capacidadeCaminhao)
print("Caixas restantes:", restoCaixas)

fatProjeto = 15000
custoFixo = 5000
percImposto = 0.15
imposto = fatProjeto * percImposto
lucro = fatProjeto - custoFixo - imposto
margemLucro = (lucro / fatProjeto)
print("Faturamento..: R$", f"{fatProjeto:,.2f}")
print("Lucro........: R$", f"{lucro:,.2f}")
print("Margem de lucro: ", f"{margemLucro:.2%}")
metaAtingida = (margemLucro > 0.3)
print("Meta atingida...:", metaAtingida)

duracao = 40
anos = duracao // 12
meses = duracao % 12
print("Duração do contrato:", anos, "anos e", meses, "meses")

faturamento = 45000 
custo = 23500
lucro = faturamento - custo
margemLucro = (lucro / faturamento)
print("Lucro........: R$", f"{lucro:,.2f}")
print("Margem de lucro: ", f"{margemLucro:.0%}")

nome = " mArCoS aNtOnIo rOcHa "
nomeFormatado = nome.strip().title()

email = " MARCOS.ROCHA@GMAIL.COM "
emailFormatado = email.strip().lower()
