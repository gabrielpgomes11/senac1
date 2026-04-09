a=5
b=1
try:
    print()
except NameError as erro:
    print("Cabeção!")
except ZeroDivisionError as erro:
    print("Divisão por zero!")
except Exception as erro:
    print("Ocorreu um erro inesperado...")
else:
    print("Operação realizada com sucesso!")
finally:
    print("Fim da operação.")