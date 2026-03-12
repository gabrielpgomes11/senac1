#26/2/2026
'''class calculadoraDobro:
    def __init__(self, numero):
        self.numero = numero

    def calcularDobro(self):
        return self.numero * 2
    

numero = float(input("Digite um número: "))
calculadora = calculadoraDobro(numero)
dobro = calculadora.calcularDobro()
print(f"O dobro de {numero} é {dobro}")


class carro: 
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

c1 = carro("Toyota", "Corolla", 2020)
c2 = carro("Honda", "Civic", 2026)
c3 = carro("Hyundai", "HB20", 2024)
for x in (c1,c2,c3):
    print(x.marca, x.modelo, x.ano)


class Pessoa:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

    def printname(self):
        print(self.fname, self.lname)
    
class Estudante(Pessoa):
    def __init__(self, fname, lname, matricula):
        super().__init__(fname, lname)
        self.matricula = matricula
    def vinculo(self):
        print("A matrícula do estudante é:", self.matricula)


p = Pessoa("José", "Silva")
p.printname()
s = Estudante("Ana", "Beatriz", 123456)
s.printname()
s.vinculo()


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print("Direção!")

class barco:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def mover(self):
        print("Vela!")

class Aviao:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

    def mover(self):
        print("Voo!")

carro1 = Carro("Ford", "Fiesta")
carro2 = Carro("Fiat", "Strada")
barco1 = barco("Ibiza", "Touring 20")
aviao1 = Aviao("Cessna", "Gran Caravan")

for x in (carro1, carro2, barco1, aviao1):
    x.mover()'''


class Pagamento:
    def __init__(self, notaFiscal, valor):
        self.notaFiscal = notaFiscal
        self.valor = valor

class PIX(Pagamento):
    def __init__(self, notaFiscal, valor, qrCode):
        super().__init__(notaFiscal, valor)
        self.qrCode = qrCode
    def desconto(self):
        print(f"{self.notaFiscal} PIX - Aplicar desconto de 15%")
    
class Boleto(Pagamento):
    def __init__(self, notaFiscal, valor, codigoBarras):
        super().__init__(notaFiscal, valor)
        self.codigoBarras = codigoBarras
    def desconto(self):
        print(f"{self.notaFiscal} Boleto - Aplicar desconto de 10%")

class Cartao(Pagamento):
    def __init__(self, notaFiscal, valor, numeroCartao):
        super().__init__(notaFiscal, valor)
        self.numeroCartao = numeroCartao
    def desconto(self):
        print(f"{self.notaFiscal} Cartão - Sem desconto!")
        
c1 = PIX(1501, 100.0, "443543597845738347539503483512343")
c2 = Boleto(1502, 200.0, "12345678901234567890123456789012345678901234")
c3 = Cartao(1503, 300.0, "1234 5678 9012 3456")

for compras in (c1, c2, c3):
    compras.desconto()