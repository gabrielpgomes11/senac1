import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

senha = "123456"
usuario = "gabriel"
def executar_programa(nome_arquivo):
    """Função para abrir um script Python externo."""
    try:
        # sys.executable garante que usaremos o mesmo interpretador Python atual
        subprocess.Popen([sys.executable, nome_arquivo])
    except FileNotFoundError:
        messagebox.showerror("Erro", f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o programa: {e}")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Meu Menu de Programas")
janela.geometry("300x250")
# Título visual
label_titulo = tk.Label(janela, text="Digite o usuário e senha", font=("Arial", 10, "bold"))
label_titulo.pack(pady=20)
label_usuario = tk.Label(janela, text="Usuário:", font=("Arial", 10))
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(janela, font=("Arial", 12))
entry_usuario.pack(pady=5)
label_senha = tk.Label(janela, text="Senha:", font=("Arial", 10))
label_senha.pack(pady=5)
entry_senha = tk.Entry(janela, font=("Arial", 12), show="*")
entry_senha.pack(pady=5)

def verificar():
    if entry_usuario.get() == usuario and entry_senha.get() == senha:
        messagebox.showinfo("Acesso permitido", "Informações corretas.")
        janela.destroy()
        executar_programa("menu.py")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretas. Tente novamente.")
        entry_usuario.delete(0, tk.END)
        entry_senha.delete(0, tk.END)


btn_verificar = tk.Button(janela, text="Verificar", command=verificar)
btn_verificar.pack(pady=10)

janela.mainloop()