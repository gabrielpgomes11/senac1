import math
import os
#os.system("cls" if os.name == "nt" else "clear")


def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Raiz Quadrada")
        print("7 - Porcentagem")
        print("8 - Resto da Divisão")
        print("9 - Divisão Inteira")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            print("Encerrando calculadora...")
            break
        
        if opcao in ["1","2","3","4","5","7","8","9"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        
        if opcao == "1":
            calcSoma = num1 + num2
            if calcSoma.is_integer():
                calcSoma = int(calcSoma)
            print("Resultado:", calcSoma)
            os.system('pause')
        
        elif opcao == "2":
            calcSub = num1 - num2
            if calcSub.is_integer():
                calcSub = int(calcSub)
            print("Resultado:", calcSub)
            os.system('pause')
        
        elif opcao == "3":
            calcMult = num1 * num2
            if calcMult.is_integer():
                calcMult = int(calcMult)
            print("Resultado:", calcMult)
            os.system('pause')
        
        elif opcao == "4":
            if num2 != 0:
                calcDiv = num1 / num2
                if calcDiv.is_integer():
                    calcDiv = int(calcDiv)
                print("Resultado:", calcDiv)
                os.system('pause')
            else:
                print("Erro: divisão por zero!")
                os.system('pause')
        
        elif opcao == "5":
            calcPot = num1 ** num2
            if calcPot.is_integer():
                calcPot = int(calcPot)
            print("Resultado:", calcPot)
            os.system('pause')
        
        elif opcao == "6":
            num = float(input("Digite o número: "))
            os.system('pause')
            if num >= 0:
                if math.sqrt(num).is_integer():
                    print("Resultado:", int(math.sqrt(num)))
                    os.system('pause')
                else:
                    print("Resultado:", math.sqrt(num))
                    os.system('pause')
            else:
                print("Erro: não existe raiz de número negativo!")
                os.system('pause')
        
        elif opcao == "7":
            calcPorcentagem = (num1 * num2) / 100
            if calcPorcentagem.is_integer():
                calcPorcentagem = int(calcPorcentagem)
            print("Resultado:", calcPorcentagem)
            os.system('pause')
        
        elif opcao == "8":
            if num2 != 0:
                calcResto = num1 % num2
                if calcResto.is_integer():
                    calcResto = int(calcResto)
                print("Resultado:", calcResto)
                os.system('pause')
            else:
                print("Erro: divisão por zero!")
                os.system('pause')
        
        elif opcao == "9":
            if num2 != 0:
                calcDivInt = num1 // num2
                if calcDivInt.is_integer():
                    calcDivInt = int(calcDivInt)
                print("Resultado:", num1 // num2)
                os.system('pause')
            else:
                print("Erro: divisão por zero!")
                os.system('pause')
                
        
        else:
            print("Opção inválida!")
            os.system('pause')

calculadora()