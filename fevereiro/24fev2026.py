#24/2/2026
'''class Pessoa:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario
    def get_salario(self):
        return self.__salario
    def set_salario(self, salario):
        if 0 < salario <= 10000:          # Verificando se o salário é um valor positivo e abaixo do teto antes de atribuí-lo
            self.__salario = salario
        else:
            print("Salário zerado ou acima do teto!")


p1 = Pessoa("Yago", 1000)
print(p1.nome)
#print(p1._Pessoa__salario)      # Acessando o atributo privado usando a convenção de nomenclatura (Não recomendado, mas possível)
#print(p1.get_salario())            # Acessando o atributo privado usando um método público da classe 
p1.set_salario(10000)                  # Modificando o valor do atributo privado usando um método público da classe 
print(p1.get_salario())                   # Verificando se o valor do salário foi atualizado corretamente após a tentativa de modificação com um valor acima do teto
'''

class Calculadora:
    def __init__(self):
        self.resultado = 0
    def __validacao(self, numero):
        if not isinstance(numero, (int, float)):
            return False
        else:
            return True
    def adicionar(self, numero):
        if self.__validacao(numero) == True:
            self.resultado += numero
        else:
            print("Número inválido!")

calc = Calculadora()
add = 1
while add != 0:
    add = float(input("Digite um número para adicionar (0 para parar): "))
    if add != 0:
        calc.adicionar(add)
add = str(add)
add = add.replace(".00", "")
print(f"O resultado final é: {calc.resultado}")

'''calc = Calculadora()
calc.adicionar("a")
calc.adicionar(10)
print(calc.resultado)


def validar_numero(numero):
    if isinstance(numero, int):
        return True
    else:
        return False'''

'''class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

livro1 = Livro("1984", "George Orwell")
print(f"Livro: {livro1.titulo}, Autor: {livro1.autor}")'''



