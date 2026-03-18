import tkinter as tk
from tkinter import messagebox

def converter_celsius_para_fahrenheit():
    """Função para processar o evento do botão"""
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_resultado.config(text=f"{fahrenheit:.2f} °F", fg="blue")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número válido.")

# 1. Criação da Janela Principal
janela = tk.Tk()
janela.title("Aula de GUI - Conversor")
janela.geometry("300x200")

# 2. Widgets (Componentes)
label_instrucao = tk.Label(janela, text="Digite a temperatura em Celsius:", font=("Arial", 10))
label_instrucao.pack(pady=10)

entry_celsius = tk.Entry(janela, font=("Arial", 12))
entry_celsius.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter", command=converter_celsius_para_fahrenheit, bg="lightgray")
botao_converter.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

# 3. Loop Principal (Mantém a janela viva)
janela.mainloop()