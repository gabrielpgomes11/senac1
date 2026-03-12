import mysql.connector
import os   
from mysql.connector import Error, errorcode 
try:
    conexao = mysql.connector.connect(
        host="localhost",
        database="dbgabriel",
        user="root",
        password="",
        connection_timeout=10)
except Error as erro:
    if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha incorretos.")
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não encontrado.")
    else:
        print("Ocorreu um erro ao conectar ao banco de dados:", erro)

if conexao.is_connected():
    input("Conexão bem-sucedida! Tecle [Enter] para continuar.")
    os.system('cls')
    cursor = conexao.cursor()

comando = f"select * from produto"

opcao = 1
while opcao != 0:
    opcao = int(input("Escolha sua opção: \n 1 - Listar produtos \n 2 - Alterar produto \n 3 - Excluir produto \n 4 - Listar  \n 5 - Limpar Tabela \n 0 - Sair: "))
    if opcao == 1:
        vdescricao = input("Digite o nome do produto: ")
        if vdescricao == "":
            input("A descrição do produto é obrigatória. Tecle [Enter] para continuar.")
        else:
            vquantidade = int(input("Digite a quantidade do produto: "))
            vpreco = float(input("Digite o valor unitário do produto: "))
            try:
                comando = f"insert into produto (descricao, quantidade, valorUnitario) values ('{vdescricao}', {vquantidade}, {vpreco})"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao cadastrar o produto:", erro)
            else:
                input("Produto cadastrado com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    elif opcao == 2:
        vid = int(input("Digite o ID do produto: "))
        if vid != 0:
            vdescricao = input("Digite a nova descrição: ")
            vquantidade = int(input("Digite a nova quantidade: "))
            vpreco = float(input("Digite o novo valor unitário: "))
            try:
                comando = f"update produto set descricao= '{vdescricao}', quantidade= {vquantidade}, valorUnitario= {vpreco} where id= {vid}"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao alterar o produto:", erro)
            else:
                input("Produto alterado com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    elif opcao == 3:
        vid = int(input("Digite o ID do produto: "))
        if vid != 0:
            try:
                comando = f"delete from produto where id= {vid}"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao excluir o produto:", erro)
            else:
                input("Produto excluído com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    elif opcao == 4:
        comando = f"select * from produto"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        input("Tecle [Enter] para continuar.")
        os.system('cls')

    elif opcao == 5:
        confirma = input("Tem certeza que deseja limpar a tabela? (s/n): ")
        if confirma.lower() == 's':
            try:
                comando = f"delete from produto"
                cursor.execute(comando)
                conexao.commit()
            except Exception as erro:
                print("Ocorreu um erro ao limpar a tabela:", erro)
            else:
                input("Tabela limpa com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    elif opcao == 0:
        print("Saindo do programa...")
    else:
        input("Opção inválida. Tecle [Enter] para continuar.")
        os.system('cls')

cursor.close()
conexao.close()