import mysql.connector
import os

conexao = mysql.connector.connect(
    host="localhost",
    database="dbgabriel",
    user="root",
    password=""
)

if conexao.is_connected():
    input("Conexão bem-sucedida! Tecle [Enter] para continuar.")
    os.system('cls')
    cursor = conexao.cursor()

opcao = 1
while opcao != 0:
    try:
        opcao = int(input("Escolha sua opção: \n 1 - Cadastrar Clientes \n 2 - Cadastrar Apartamentos \n 3 - Cadastrar Reservas \n 4 - Listar Reservas \n 0 - Sair: \n"))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        os.system('cls')
        continue

    if opcao == 1:
        vnome = input("Digite o nome do cliente: ")
        if vnome == "":
            input("O nome do cliente é obrigatório. Tecle [Enter] para continuar.")
        else:
            vcpf = input("Digite o CPF do cliente: ")
            vtelefone = input("Digite o telefone do cliente: ")
            vemail = input("Digite o email do cliente: ")
            try:
                comando = f"insert into clientes (nome, cpf, celular, email) values ('{vnome}', '{vcpf}', '{vtelefone}', '{vemail}')"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao cadastrar o cliente:", erro)
                input("Tecle [Enter] para continuar.")
                os.system('cls')
            else:
                input("Cliente cadastrado com sucesso! Tecle [Enter] para continuar.")
                os.system('cls')

    if opcao == 2:
        vnumero = input("Digite o número do apartamento: ")
        if vnumero == "":
            input("O número do apartamento é obrigatório. Tecle [Enter] para continuar.")
        else:
            vtipo = input("Digite o tipo do apartamento: ")
            vpreco = float(input("Digite o preço do apartamento: "))
            try:
                comando = f"insert into apartamentos (numeroAp, categoria, valorDiaria) values ('{vnumero}', '{vtipo}', {vpreco})"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao cadastrar o apartamento:", erro)
                os.system('cls')
            else:
                input("Apartamento cadastrado com sucesso! Tecle [Enter] para continuar.")
                os.system('cls')

    if opcao == 3:
        vcpf = int(input("Digite o CPF do cliente: "))
        vnumeroAp = int(input("Digite o número do apartamento: "))
        vdata_entrada = input("Digite a data de entrada: ")
        vdata_saida = input("Digite a data de saída: ")
        try:
            comando = f"insert into reserva (CPF, numeroAp, dataEntrada, dataSaida) values ({vcpf}, {vnumeroAp}, '{vdata_entrada}', '{vdata_saida}')"
            cursor.execute(comando)
            conexao.commit()
        except Exception as erro:
            print("Ocorreu um erro ao cadastrar a reserva:", erro)
            
        else:
            input("Reserva cadastrada com sucesso! Tecle [Enter] para continuar.")
            
    
    if opcao == 4:
        try:
            comando = f"select * from reserva"
            cursor.execute(comando)
            resultado = cursor.fetchall()
        except Exception as erro:
            print("Ocorreu um erro ao listar a reserva:", erro)
            os.system('cls')
        else:
            for linha in resultado:
                print(linha)
            input("Tecle [Enter] para continuar.")
            os.system('cls')
    
    if opcao == 0:
        input("Encerrando o programa. Tecle [Enter] para continuar.")
        os.system('cls')
        break

cursor.close()
conexao.close()