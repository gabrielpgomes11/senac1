# 3/2/2026
print(f"Olá! Esse é o meu primeiro programa.")
nome=input("Digite seu nome: ")
print("Olá, meu nome é " + nome)

v_numero1=int(input("Digite um número: "))
v_numero2=int(input("Digite um número: "))
v_soma=(v_numero1+v_numero2)
print("O resultado é",v_soma)

v1numero1=float(input("Digite o primeiro número: "))
v1numero2=float(input("Digite o segundo número: "))
v1numero3=float(input("Digite o terceiro número: "))
v1soma=(v1numero1+v1numero2+v1numero3)
v1media=(v1soma/3)
print("A média dos números é:", v1media)

numero=int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

idade=int(input("Digite sua idade: "))
if idade > 17:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

v2nota1=float(input("Digite a primeira nota: "))
v2nota2=float(input("Digite a segunda nota: "))
v2nota3=float(input("Digite a terceira nota: "))
v2media=(v2nota1+v2nota2+v2nota3)/3
print("Média:", v2media)
if v2media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
