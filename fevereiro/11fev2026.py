valor =input("Insira o valor a investir: ")
valor = valor.replace("R$ ", "").replace(".", "").replace(",", ".")
valor = float(valor)
if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto.")
elif valor <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários.")
else:
    print("Perfil arrojado: Sugerimos Ações.")
print("Vamos prosseguir com o investimento?")

admins = ["ana@empresa.com.br", "guilherme@empresa.com.br", "felipe@empresa.com.br"]
email = input("Digite seu email para acessar o sistema: ")
email = email.strip().lower()
if email in admins:
    print("Acesso liberado! Bem vindo ao painel de controle.")
else:
    print("Acesso negado. Você não tem permissões de administrador.")

compra = int(input("Digite o valor da compra: "))

if compra < 200:
    percDesconto = 0
elif compra < 500:
    percDesconto = 0.1
else:
    percDesconto = 0.15
desconto = compra * percDesconto
valorFinal = compra - desconto
print(f"Valor da compra: R${compra:,.2f}\n Desconto aplicado:R${desconto:,.2f}\n Valor final: R${valorFinal:,.2f}")

#minha versão
vendaVendedor = (input("Digite o valor total das vendas do vendedor: "))
metaVendedor = (input("Digite a meta de vendas do vendedor: "))
vendaLoja = (input("Digite o valor total das vendas da empresa: "))
metaLoja = (input("Digite a meta de vendas da empresa: "))
percBonus = 0

vendaVendedor = vendaVendedor.replace("R$ ", "").replace(".", "").replace(",", ".")
vendaLoja = vendaLoja.replace("R$ ", "").replace(".", "").replace(",", ".")
metaVendedor = metaVendedor.replace("R$ ", "").replace(".", "").replace(",", ".")
metaLoja = metaLoja.replace("R$ ", "").replace(".", "").replace(",", ".")

if float(vendaVendedor) >= float(metaVendedor) and float(vendaLoja) >= float(metaLoja):
    print("Parabéns! Você atingiu sua meta e a meta da empresa!")
    percBonus = 0.20
else:
    print("Seu bônus esse mês é de R$0,00.")

bonus = float(vendaVendedor) * percBonus
print(f"Valor do bônus: R${bonus:,.2f} \n Valor total recebido: R${float(vendaVendedor) + bonus:,.2f}")

#versao do Marcelo
vendas_vendedor = float(input("Digite o valor total das vendas do vendedor: "))
meta_vendedor = float(input("Digite a meta de vendas do vendedor: "))

vendas_loja = float(input("Digite o valor total das vendas da empresa: "))
meta_loja = float(input("Digite a meta de vendas da empresa: "))

if vendas_loja > meta_loja and vendas_vendedor > meta_vendedor:
    bonus = (vendas_vendedor * 0.2)
else:
    bonus = 0
print(f"Seu bônus este mês é de: R${bonus:,.2f}")


assuntoEmail = input("Escreva o assunto do email: ")
assuntoEmail = assuntoEmail.lower()
if "pagamento" in assuntoEmail or "boleto" in assuntoEmail:
    print("Encaminhado para o Financeiro.")
elif "entrega" in assuntoEmail or "atraso" in assuntoEmail:
    print("Encaminhado para a Logística.")
else:
    print("Encaminhado para o Suporte Geral.")


clientes = {"Gabriel": 5000, "Letícia": 3000, "Othávio": 4500}
novaCompra = 1500
clientes["Letícia"] = (clientes["Letícia"] + novaCompra)
clientes["Matheus"] = 2000
print(clientes)
#print(*clientes, sep="\n")
for item in clientes:
   print(item)

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input("Digite o nome do produto: ")
produto = produto.strip().lower()
if produto in estoque:
    print(f"{produto} encontrado: {estoque[produto]} unidades em estoque.")
else:
    print("Produto não encontrado no sistema.")
