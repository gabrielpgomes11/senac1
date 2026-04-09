'''class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"
    def basico(self):
        print(f"Livro: {self.titulo}, Autor: {self.autor}")
    def detalhes(self):
        print(f"Detalhes:\n Ano: {self.ano}, Gênero: {self.genero}")


livro1 = Livro("1984", "George Orwell", 1948, "Distopia")
livro1.basico()
acao = input("Deseja ver os detalhes do livro? (s/n): ").strip().lower()
if acao == 's':
    livro1.detalhes()
elif acao == 'n':
    print("Ok, detalhes não exibidos.")
else:
    print("Opção inválida! Detalhes não exibidos.")

class Cachorro:
    def latir(self):
        print("Au au!")

Cachorro1 = Cachorro()
Cachorro1.latir()

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        area = self.largura * self.altura
        print(f"Área: {area}")

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
retangulo1 = Retangulo(largura, altura)
retangulo1.area()

class Animal:
    def comer(self):
        print("Alimenta")

class Cachorro(Animal):
    def som(self):
        print("Late")

class Passaro(Animal):
    def som(self):
        print("Canta")

class Gato(Animal):
    def som(self):
        print("Mia")
    
ser = int(input("Escolha um animal (1-Cachorro, 2-Pássaro, 3-Gato): "))
if ser == 1:
    a1 = Cachorro()
    a1.som()
    a1.comer()
elif ser == 2:
    a2 = Passaro()
    a2.som()
    a2.comer()
elif ser == 3:
    a3 = Gato()
    a3.som()
    a3.comer()
else:
    print("Animal inválido!")'''

class contaBancaria:
    def __init__(self, saldoInicial):
        self.saldo = saldoInicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        
    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
    
    def exibirSaldo(self):
        return self.saldo

quantia = contaBancaria(0)
#quantia.depositar(100.00)
#quantia.depositar(200.00)
#quantia.retirar(50.00)
#print(quantia.exibirSaldo())

opcao = 1
while opcao != 0:
    opcao = int(input("Escolha uma opção: 1-Depositar, 2-Retirar, 0-Sair: "))
    if opcao != 0:
        valor = float(input("Digite o valor: "))
        if opcao == 1:
            quantia.depositar(valor)
        if opcao == 2:
            if valor > quantia.exibirSaldo():
                print("Saldo insuficiente!")
            else:
                quantia.retirar(valor)
        print(f"Saldo atualizado: {quantia.exibirSaldo():,.2f}")
