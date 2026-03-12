#13fev2026


def calcularIss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
    imposto = (valor * taxa)
    return imposto

valorNota = float(input("Digite o valor da nota: "))
print(f"{calcularIss(valorNota):,.2f}")


produtosBaguncados = ['Iphone 13', 'MACBOOK PRO', 'aIrPoDs Pro', 'IPad mini', 'caixa de som bluetooth']

def padronizarTexto(texto):
    texto = texto.strip()
    texto = texto.title()
    return texto

produtosPadronizados = []
for produto in produtosBaguncados:
    prodPadronizado = padronizarTexto(produto)
    produtosPadronizados.append(prodPadronizado)

print(produtosPadronizados)


def analisarMargem(faturamento, custo):
    lucro = (faturamento - custo)
    margem = (lucro / custo)
    if margem >= 0.3:
        return "Margem saudável"
    else:
        return "Margem baixa"

faturamento = float(input("Digite o valor do faturamento: "))
custo = float(input("Digite o valor do custo: "))
print(analisarMargem(faturamento,custo))


def quemBateuMeta(vendaVendedores: dict, meta: float):
    for vendedor in vendaVendedores:
        if vendaVendedores[vendedor] >= meta:
            print(f"Vendedor {vendedor} bateu a meta!")



equipeVendas = {'João': 12000, 'Maria': 9500, 'Ricardo': 10000, 'Fernanda': 15200, 'Paulo': 5000}
metaVendas = 10000
quemBateuMeta(equipeVendas, metaVendas)


def converterParaReal(valorDolar, cotacaoDolar):    #Função de conversão 
    valorReal = (valorDolar * cotacaoDolar)
    return valorReal

def processarListaPrecos(listaPrecosDolar, cotacaoDolar):   # Percorre a lista e chama a função de conversão
    for item in listaPrecosDolar:
        valorReais = converterParaReal(item, cotacaoDolar)
        print(f"O item custa US${item} e em reais: R${valorReais}")

precosUSD = [100, 50, 250]
cotacao = 5.20
processarListaPrecos(precosUSD, cotacao)

