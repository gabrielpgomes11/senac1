import tkinter as tk
from tkinter import messagebox

def calcularIMC():
    """Função para processar o evento do botão"""
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if altura <= 0:
            messagebox.showerror("Erro de Entrada", "A altura deve ser maior que zero.")
            return
        
        imc = peso / (altura ** 2)
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número válido.")

# 1. Criação da Janela Principal
janela = tk.Tk()
janela.title("Aula de GUI - Calcular IMC")
janela.geometry("300x200")

# 2. Widgets (Componentes)
label_instrucao = tk.Label(janela, text="Digite o peso (em kg):", font=("Arial", 10))
label_instrucao.pack(pady=10)

entry_peso = tk.Entry(janela, font=("Arial", 12))
entry_peso.pack(pady=5)

label_altura = tk.Label(janela, text="Digite a altura (em metros):", font=("Arial", 10))
label_altura.pack(pady=10)

entry_altura = tk.Entry(janela, font=("Arial", 12))
entry_altura.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcularIMC, bg="lightgray")
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

# 3. Loop Principal (Mantém a janela viva)
janela.mainloop()