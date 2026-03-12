#12fev2026
vendasRegiao = {
    'Norte': 15000,
    'Sul': 22000,
    'Leste': 18000,
    'Oeste': 25000
}   
listaVendas = list(vendasRegiao.values())
totalVendas = sum(listaVendas)
qtdVendas = len(listaVendas)
mediaVendas = (totalVendas / qtdVendas)
print("Total de vendas: ", totalVendas)
print("Média de vendas: ", mediaVendas)


desempenho = {
    'Lira': [8, 9, 7],
    'Paula': [10, 9, 10],
    'Tiago': [6, 7, 8]
}
nome = input("Digite o nome do colaborador: ").title()
nota = desempenho[nome]
print(f"Nome: {nome}")
print(f"Nota: {nota}")
media = sum(nota) / len(nota)
print(f"Média: {media:,.2f}")


produtos = {
    'celular': 1500,
    'camera': 800,
    'radio': 200,
    'fone': 100
}
itemRemovido = "celular"
produtos.pop(itemRemovido)
celularNoDic = "celular" in produtos
print("Celular no estoque: ", celularNoDic)


for i in range(10):
    tempoFalta = 10 - i
    print(f"Faltam {tempoFalta} minutos para começar o treinamento")


vendas = [2000, 5000, 1000, 8000, 3000]
comissaoTotal = 0
for venda in vendas:
    if venda > 4000:
        comissao = 0.1
    else:
        comissao = 0.05
    comissaoTotal = comissaoTotal + (venda * comissao)
print(f"Comissão total: R$ {comissaoTotal:,.2f}")


estoque = {
    'monitor': 5,
    'teclado': 12,
    'mouse': 2,
    'headset': 8,
    'gabinete': 15
}
produto = estoque.keys()
for p in produto:
    if estoque[p] < 8:
        print(f"ALERTA! O produto {p} está com apenas {estoque[p]} unidades em estoque!")

metas = {
    'jan': 1000,
    'fev': 1200,
    'mar': 1100
} 
gastos = { 
    'jan': 900,
    'fev': 1350,
    'mar': 1100
}
for mes in gastos:
    if gastos[mes] > metas[mes]:
        diferenca = gastos[mes] - metas[mes]
        print(f"Mês {mes}: Orçamento estourado em R${diferenca};")
    else:
        print(f"Mês {mes}: Dentro do orçamento.")


precos = {
    'celular': 1500,
    'tablet': 2500,
    'notebook': 5000
}
print(precos)
percAumento = input("Qual o percentual de aumento(%): ")
percAumento = percAumento.replace("%", "")
percAumento = float(percAumento) / 100
for produto in precos:
    precos[produto] = float((precos[produto] * (1 + percAumento)))
    precos[produto] = f"{precos[produto]:,.2f}"
print(precos)