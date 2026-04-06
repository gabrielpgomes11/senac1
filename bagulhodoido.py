import random

produtos = ["Mouse", "Teclado", "Monitor", "SSD", "RAM", "Gabinete", "Fonte", "Cabo", "Webcam", "Headset"]
marcas = ["Logitech", "Razer", "HyperX", "Samsung", "Asus", "Corsair", "Dell", "HP"]

with open("popula_produtos.sql", "w", encoding="utf-8") as f:
    for i in range(1, 501):
        codigo = 7891000000 + i
        desc = f"{random.choice(produtos)} {random.choice(marcas)} Pro {random.randint(1,9)}"
        estoque = random.randint(5, 200)
        preco = round(random.uniform(20.0, 3500.0), 2)
        
        f.write(f"INSERT INTO produto (codigo, descricao, quantidade_estoque, valor_unitario) "
                f"VALUES ({codigo}, '{desc}', {estoque}, {preco:.2f});\n")

print("Arquivo 'popula_produtos.sql' gerado com sucesso!")