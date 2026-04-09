import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',         # Seu usuário do MySQL
            password='password', # Sua senha do MySQL
            database='hotel_db'
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

# --- FUNÇÕES GENÉRICAS DE CRUD ---

def executar_query(query, valores=None, multi=False):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, valores)
            if multi:
                resultados = cursor.fetchall()
                return resultados
            conn.commit()
            print("Operação realizada com sucesso!")
        except Error as e:
            print(f"Erro: {e}")
        finally:
            conn.close()

# --- ENTIDADE: CLIENTE ---

def incluir_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cel = input("Celular: ")
    email = input("Email: ")
    executar_query("INSERT INTO cliente (nome, cpf, celular, email) VALUES (%s, %s, %s, %s)", (nome, cpf, cel, email))

def listar_clientes():
    res = executar_query("SELECT * FROM cliente", multi=True)
    for r in res: print(r)

def alterar_cliente():
    cpf = input("Digite o CPF do cliente a alterar: ")
    novo_nome = input("Novo nome: ")
    executar_query("UPDATE cliente SET nome=%s WHERE cpf=%s", (novo_nome, cpf))

def excluir_cliente():
    cpf = input("Digite o CPF do cliente a excluir: ")
    executar_query("DELETE FROM cliente WHERE cpf=%s", (cpf,))

# --- ENTIDADE: APARTAMENTO ---

def incluir_apartamento():
    num = int(input("Número: "))
    cat = input("Categoria: ")
    valor = float(input("Valor Diária: "))
    executar_query("INSERT INTO apartamento (numero, categoria, valor_diaria) VALUES (%s, %s, %s)", (num, cat, valor))

def listar_apartamentos():
    res = executar_query("SELECT * FROM apartamento", multi=True)
    for r in res: print(r)

# --- ENTIDADE: RESERVA ---

def incluir_reserva():
    cpf = input("CPF do Cliente: ")
    num_apt = int(input("Número do Apartamento: "))
    entrada = input("Data Entrada (AAAA-MM-DD): ")
    saida = input("Data Saída (AAAA-MM-DD): ")
    executar_query("INSERT INTO reserva (cpf_cliente, num_apartamento, data_entrada, data_saida) VALUES (%s, %s, %s, %s)",
                   (cpf, num_apt, entrada, saida))

def listar_reservas():
    res = executar_query("SELECT * FROM reserva", multi=True)
    for r in res: print(r)

# --- MENU PRINCIPAL ---

def menu():
    while True:
        print("\n--- SISTEMA DE RESERVAS HOTEL ---")
        print("1. Gerenciar Clientes (Incluir/Listar/Alterar/Excluir)")
        print("2. Gerenciar Apartamentos (Incluir/Listar)")
        print("3. Gerenciar Reservas (Incluir/Listar)")
        print("0. Sair")
       
        opcao = input("Escolha: ")
       
        if opcao == '1':
            print("a.Incluir b.Listar c.Alterar d.Excluir")
            sub = input("Opção: ")
            if sub == 'a': incluir_cliente()
            elif sub == 'b': listar_clientes()
            elif sub == 'c': alterar_cliente()
            elif sub == 'd': excluir_cliente()
        elif opcao == '2':
            print("a.Incluir b.Listar")
            sub = input("Opção: ")
            if sub == 'a': incluir_apartamento()
            elif sub == 'b': listar_apartamentos()
        elif opcao == '3':
            print("a.Incluir b.Listar")
            sub = input("Opção: ")
            if sub == 'a': incluir_reserva()
            elif sub == 'b': listar_reservas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()