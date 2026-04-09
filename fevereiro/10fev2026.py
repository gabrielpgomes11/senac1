# 10/2/2026
email="andre_silva@empresa.com.br"
email=email.strip().lower().replace("@empresa.com.br", "@grupocorp.com")
print(email)

email="beatriz.oliveira@grupocorp.com"
email=email.partition('@')[0]
print(email)

nome="lucas ferreira souza"
nome=nome.split()[0].capitalize()
print("Olá,", nome +", bem-vindo ao nosso grupo!")

vendas = 1500, 2000, 800, 3500, 1200
totalVendas = sum(vendas)
qtdVendas = len(vendas)
mediaVendas = totalVendas / len(vendas)
maiorvenda = max(vendas)
menorvenda = min(vendas)
print(f"Total de vendas: R$ {totalVendas:,.2f}")
print(f"Quantidade de vendas: {qtdVendas}")
print(f"Média de vendas: R$ {mediaVendas:,.2f}")
print(f"Maior venda: R$ {maiorvenda:,.2f}")
print(f"Menor venda: R$ {menorvenda:,.2f}")

estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
posTeclado = estoque.index("teclado")
estoque[posTeclado] = "teclado mecânico"
impEstoque = "impressora" in estoque
estoque.remove("mouse")
print("Impressora está no estoque?", impEstoque)
print("Produtos em estoque:", estoque)

fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
topFretes = fretes[:2]
print("Todos os fretes..:", fretes)
print("Fretes mais caros:", topFretes)

rota = ["São Paulo", "Campinas", "Jundiaí", "Sorocaba"]
novasCidades = ["Itu", "Valinhos"]
rota.extend(novasCidades)
print(rota)
posSorocaba = rota.index("Sorocaba") + 1
print(f"Sorocaba é a {posSorocaba}° cidade da rota")

precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]
print("ATUAL:")
print(vinhos)
print(precos)

vinhoEscolhido = input("Digite o nome do vinho que deseja atualizar o preço: ").title()
novoPreco =(input("Digite o novo preço para o vinho: "))
novoPreco = novoPreco.replace("R$ ", "").replace(".", " ").replace(",", ".")
novoPreco = float(novoPreco)

posVinho = vinhos.index(vinhoEscolhido)
precos[posVinho] = novoPreco

print("ATUALIZADO:")
print(vinhos)
print(precos)


