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
    opcao = int(input("Escolha sua opção: \n 1 - Login \n 2 - Registrar \n 3 - Alterar Registro \n 4 - Listar Usuários \n 5 - Excluir Registro \n 0 - Sair: "))
    if opcao == 1:
        vlogin = input("Digite o login: ")
        if vlogin == "":
            input("O login é obrigatório. Tecle [Enter] para continuar.")
        else:
            vsenha = input("Digite a senha: ")
            comando = f"select * from usuarios where senha= '{vsenha}' and login= '{vlogin}'"
            cursor.execute(comando)
            resultado = cursor.fetchone()
            if resultado:
                input("Login bem-sucedido! Tecle [Enter] para continuar.")
                os.system('cls')
                break
            else:
                input("Usuário ou senha incorretos. Tecle [Enter] para tentar novamente.")
                os.system('cls')

    if opcao == 2:
        vusuario = input("Digite o nome do usuário: ")
        if vusuario == "":
            input("O nome do usuário é obrigatório. Tecle [Enter] para continuar.")
        else:
            vsenha = input("Digite a senha: ")
            vlogin = input("Digite o login: ")
            comando = f"insert into usuarios (nome, senha, login) values ('{vusuario}', '{vsenha}', '{vlogin}')"
            cursor.execute(comando)
            conexao.commit()
            input("Usuário registrado com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    if opcao == 3:
        vid = int(input("Digite o ID do usuário: "))
        if vid != 0:
            vusuario = input("Digite o novo nome do usuário: ")
            vsenha = input("Digite a nova senha: ")
            vlogin = input("Digite o novo login: ")
            comando = f"update usuarios set nome= '{vusuario}', senha= '{vsenha}', login= '{vlogin}' where id= {vid}"
            cursor.execute(comando)
            conexao.commit()
            input("Registro alterado com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')

    if opcao == 4:
        comando = f"select * from usuarios"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        input("Tecle [Enter] para continuar.")
        os.system('cls')
    
    if opcao == 5:
        vid = int(input("Digite o ID do usuário: "))
        if vid != 0:
            comando = f"delete from usuarios where id= {vid}"
            cursor.execute(comando)
            conexao.commit()
            input("Registro excluído com sucesso! Tecle [Enter] para continuar.")
            os.system('cls')
    if opcao == 0:
        input("Saindo do programa...")
    else:
        input("Opção inválida. Tecle [Enter] para continuar.")
        os.system('cls')


cursor.close()
conexao.close()