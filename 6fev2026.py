# 6/2/2026
senha=int(input("Digite a senha: "))
while senha != 1234:
    print("Senha incorreta. Tente novamente.")
    senha=int(input("Digite a senha: "))
print("Senha correta. Acesso permitido.")

valorCompra=float(input("Digite o valor da compra: "))
if valorCompra >= 100:
    desconto=valorCompra*0.10
    valorFinal=valorCompra-desconto
    print("O valor final da compra é:", valorFinal)
else:
    print("Não há desconto disponível para compras abaixo de R$100,00.")

salarioBruto=float(input("Digite o salário bruto.................: "))
qtdHoraExtraDiurna=float(input("Digite a Qtd. de horas extras (Diurnas): "))
qtdHoraExtraDomFer=float(input("Digite a Qtd. de horas extras (Dom/Fer): "))
#Cálculo do valor das horas trabalhadas
vlHoraTrabalho=float(salarioBruto/220)
vlHoraExtraDiurna=float(qtdHoraExtraDiurna*(vlHoraTrabalho*1.5))
vlHoraExtraDomFer=float(qtdHoraExtraDomFer*(vlHoraTrabalho*2))
#Cálculo do INSS descontado
if salarioBruto <= 1621.00:
    inss=float(salarioBruto*0.075)
elif salarioBruto <= 2902.84:
    inss=float(salarioBruto*0.09)
elif salarioBruto <= 4351.27:
    inss=float(salarioBruto*0.12)
else:
    inss=float(salarioBruto*0.14)
print("Salário bruto..................: R$" f"{salarioBruto:,.2f}")
print("Valor das horas extras diurnas.: R$" f"{vlHoraExtraDiurna:,.2f}")
print("Valor das horas extras dom/fes.: R$" f"{vlHoraExtraDomFer:,.2f}")
print("INSS...........................: R$" f"{inss:,.2f}")
print("Salário líquido................: R$" f"{salarioBruto+vlHoraExtraDiurna+vlHoraExtraDomFer-inss:,.2f}")