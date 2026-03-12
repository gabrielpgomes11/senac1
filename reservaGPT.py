import mysql.connector

# -------------------------------
# Conexão com o banco
# -------------------------------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbgabriel"
)

cursor = con.cursor()

# -------------------------------
# CLIENTE
# -------------------------------

def incluir_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    celular = input("Celular: ")
    email = input("Email: ")

    sql = "INSERT INTO cliente (nome, cpf, celular, email) VALUES (%s,%s,%s,%s)"
    valores = (nome, cpf, celular, email)

    cursor.execute(sql, valores)
    con.commit()
    print("Cliente cadastrado!")

def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    dados = cursor.fetchall()

    for c in dados:
        print(c)

def alterar_cliente():
    cpf = input("CPF do cliente: ")
    nome = input("Novo nome: ")
    celular = input("Novo celular: ")
    email = input("Novo email: ")

    sql = """
    UPDATE cliente
    SET nome=%s, celular=%s, email=%s
    WHERE cpf=%s
    """

    valores = (nome, celular, email, cpf)
    cursor.execute(sql, valores)
    con.commit()

    print("Cliente atualizado!")

def excluir_cliente():
    cpf = input("CPF do cliente: ")

    sql = "DELETE FROM cliente WHERE cpf=%s"
    cursor.execute(sql, (cpf,))
    con.commit()

    print("Cliente excluído!")

# -------------------------------
# APARTAMENTO
# -------------------------------

def incluir_apartamento():
    numero = input("Número do apartamento: ")
    categoria = input("Categoria: ")
    valor = input("Valor da diária: ")

    sql = "INSERT INTO apartamento (numero, categoria, valor_diaria) VALUES (%s,%s,%s)"
    cursor.execute(sql, (numero, categoria, valor))
    con.commit()

    print("Apartamento cadastrado!")

def listar_apartamentos():
    cursor.execute("SELECT * FROM apartamento")
    dados = cursor.fetchall()

    for a in dados:
        print(a)

def alterar_apartamento():
    numero = input("Número do apartamento: ")
    categoria = input("Nova categoria: ")
    valor = input("Novo valor da diária: ")

    sql = """
    UPDATE apartamento
    SET categoria=%s, valor_diaria=%s
    WHERE numero=%s
    """

    cursor.execute(sql, (categoria, valor, numero))
    con.commit()

    print("Apartamento atualizado!")

def excluir_apartamento():
    numero = input("Número do apartamento: ")

    sql = "DELETE FROM apartamento WHERE numero=%s"
    cursor.execute(sql, (numero,))
    con.commit()

    print("Apartamento excluído!")

# -------------------------------
# RESERVA
# -------------------------------

def incluir_reserva():
    cpf = input("CPF do cliente: ")
    apt = input("Número do apartamento: ")
    entrada = input("Data de entrada (AAAA-MM-DD): ")
    saida = input("Data de saída (AAAA-MM-DD): ")

    sql = """
    INSERT INTO reserva (cpf_cliente, num_apartamento, data_entrada, data_saida)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(sql, (cpf, apt, entrada, saida))
    con.commit()

    print("Reserva cadastrada!")

def listar_reservas():
    cursor.execute("SELECT * FROM reserva")
    dados = cursor.fetchall()

    for r in dados:
        print(r)

def alterar_reserva():
    id_reserva = input("ID da reserva: ")
    entrada = input("Nova data de entrada: ")
    saida = input("Nova data de saída: ")

    sql = """
    UPDATE reserva
    SET data_entrada=%s, data_saida=%s
    WHERE id=%s
    """

    cursor.execute(sql, (entrada, saida, id_reserva))
    con.commit()

    print("Reserva atualizada!")

def excluir_reserva():
    id_reserva = input("ID da reserva: ")

    sql = "DELETE FROM reserva WHERE id=%s"
    cursor.execute(sql, (id_reserva,))
    con.commit()

    print("Reserva excluída!")

# -------------------------------
# MENU
# -------------------------------

def menu():
    while True:

        print("\n===== SISTEMA HOTEL =====")
        print("1 - Cliente")
        print("2 - Apartamento")
        print("3 - Reserva")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            menu_cliente()

        elif op == "2":
            menu_apartamento()

        elif op == "3":
            menu_reserva()

        elif op == "0":
            break


def menu_cliente():

    print("\n--- CLIENTE ---")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Listar")

    op = input("Escolha: ")

    if op == "1":
        incluir_cliente()

    elif op == "2":
        alterar_cliente()

    elif op == "3":
        excluir_cliente()

    elif op == "4":
        listar_clientes()


def menu_apartamento():

    print("\n--- APARTAMENTO ---")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Listar")

    op = input("Escolha: ")

    if op == "1":
        incluir_apartamento()

    elif op == "2":
        alterar_apartamento()

    elif op == "3":
        excluir_apartamento()

    elif op == "4":
        listar_apartamentos()


def menu_reserva():

    print("\n--- RESERVA ---")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Listar")

    op = input("Escolha: ")

    if op == "1":
        incluir_reserva()

    elif op == "2":
        alterar_reserva()

    elif op == "3":
        excluir_reserva()

    elif op == "4":
        listar_reservas()


# -------------------------------
# EXECUÇÃO
# -------------------------------

menu()