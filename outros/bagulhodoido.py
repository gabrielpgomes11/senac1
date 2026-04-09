import random

produtos = ["Mouse", "Teclado", "Monitor", "SSD", "RAM", "Gabinete", "Fonte", "Cabo", "Webcam", "Headset"]
marcas = ["Logitech", "Razer", "HyperX", "Samsung", "Asus", "Corsair", "Dell", "HP"]

with open("popula_funcionarios.sql", "w", encoding="utf-8") as f:
    for i in range(1, 501):
        codigo = 7891000000 + i
        desc = f"{random.choice(produtos)} {random.choice(marcas)} Pro {random.randint(1,9)}"

        f.write(f"INSERT INTO produto (codigo_produto, descricao, unidade_medida, valor_compra, valor_venda, qtd_estoque, qtd_maxima, qtd_minima) "
                f"VALUES ({codigo}, '{desc}', {unidade_medida}, {valor_compra}, {valor_venda}, {estoque}, {qtd_maxima}, {qtd_minima}); \n")

print("Arquivo 'popula_funcionarios.sql' gerado com sucesso!")