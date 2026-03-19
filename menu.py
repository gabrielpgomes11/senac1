import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def executar_programa(nome_arquivo):
    """Função para abrir um script Python externo."""
    try:
        # sys.executable garante que usaremos o mesmo interpretador Python atual
        subprocess.Popen([sys.executable, nome_arquivo])
    except FileNotFoundError:
        messagebox.showerror("Erro", f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o programa: {e}")

def funcaoFechar():
    janela.quit()

def funcaoExecutar():
    executar_programa("login_menu.py")

def funcaoWrapper():
    funcaoExecutar()
    funcaoFechar()

janela = tk.Tk()
janela.title("Meu Menu de Programas")
janela.geometry("300x250")

label_titulo = tk.Label(janela, text="Selecione um Programa", font=("Arial", 14, "bold"))
label_titulo.pack(pady=20)


btn1 = tk.Button(janela, text="Abrir Conversor", width=20,
                 command=lambda: executar_programa("temperatura.py"))
btn1.pack(pady=5)

btn2 = tk.Button(janela, text="Abrir Calculadora de IMC", width=20,
                 command=lambda: executar_programa("calculadora_imc.py"))
btn2.pack(pady=5)

btn3 = tk.Button(janela, text="Login", width=20,
                 command=lambda: funcaoWrapper())
btn3.pack(pady=5)

btn_sair = tk.Button(janela, text="Sair", width=20, fg="red", command=janela.quit)
btn_sair.pack(pady=20)

janela.mainloop()