#5/2/2026
numero = int(input("Digite um número: "))
for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")

    
class Dobro:
    def __init__(self):
        pass
    def calcular(self):
        numero = int(input("Digite um número: "))
        dobro = numero * 2
        print(f"O dobro de {numero} é {dobro}")

dobro_calculador = Dobro()
dobro_calculador.calcular()
"""
"""
calculo=1
soma=0
while calculo != 0:
    calculo = int(input("Digite um número (ou 0 para sair): "))
    soma += calculo
print(soma)

gasto_kwh=int(input("Digite o gasto (em kWh): "))
gasto_final=gasto_kwh*0.75
print("O valor total a ser pago é:",gasto_final)
"""
"""
peso=float(input("Digite seu peso (em kg): "))
altura=float(input("Digite sua altura (em metros): "))
imc=peso/(altura**2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidade grau 1")
elif imc >= 35 and imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
