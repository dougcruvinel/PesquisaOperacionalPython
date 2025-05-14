import tkinter as tk
from pulp import *
from tkinter import PhotoImage



def resolver_problema():
    # Criar o problema de programação linear (maximização)
    model = LpProblem("picole_lele", LpMaximize)
    
    # Variáveis de decisão
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    x4 = LpVariable("x4", lowBound=0)
    x5 = LpVariable("x5", lowBound=0)

    # Função objetivo
    model += (float(entrada_lucro_x1.get()) * x1) + \
             (float(entrada_lucro_x2.get()) * x2) + \
             (float(entrada_lucro_x3.get()) * x3) + \
             (float(entrada_lucro_x4.get()) * x4) + \
             (float(entrada_lucro_x5.get()) * x5), "Lucro Total"

    # Adicionar restrições de leite
    model += float(entrada_leite_x1.get()) * x1 + float(entrada_leite_x2.get()) * x2 + \
             float(entrada_leite_x3.get()) * x3 + float(entrada_leite_x4.get()) * x4 + \
             float(entrada_leite_x5.get()) * x5 <= float(entrada_max_leite.get())

    # Adicionar restrições de açúcar
    model += float(entrada_acucar_x1.get()) * x1 + float(entrada_acucar_x2.get()) * x2 + \
             float(entrada_acucar_x3.get()) * x3 + float(entrada_acucar_x4.get()) * x4 + \
             float(entrada_acucar_x5.get()) * x5 <= float(entrada_max_acucar.get())

    # Adicionar restrições de polpa de fruta
    model += float(entrada_polpa_x1.get()) * x1 + float(entrada_polpa_x2.get()) * x2 + \
             float(entrada_polpa_x3.get()) * x3 + float(entrada_polpa_x4.get()) * x4 + \
             float(entrada_polpa_x5.get()) * x5 <= float(entrada_max_polpa.get())

    # Resolver o problema
    status = model.solve()

    # Obter os nomes dos sabores
    sabores = [entrada_sabor_x1.get(), entrada_sabor_x2.get(), entrada_sabor_x3.get(),
               entrada_sabor_x4.get(), entrada_sabor_x5.get()]

    # Atualizar a janela com os resultados, convertendo para inteiros
    resultado_label.config(text=f"Resultado:\n"
                                f"Produza {int(value(x1))} unidades de {sabores[0]}\n"
                                f"Produza {int(value(x2))} unidades de {sabores[1]}\n"
                                f"Produza {int(value(x3))} unidades de {sabores[2]}\n"
                                f"Produza {int(value(x4))} unidades de {sabores[3]}\n"
                                f"Produza {int(value(x5))} unidades de {sabores[4]}\n"
                                f"Lucro máximo: R${int(value(model.objective))}\n"
                                f"Status da solução: {LpStatus[status]}")
    
    

# Criar a janela principal
janela = tk.Tk()
janela.title("Maximização de Lucro - Picolé Lelé")



# Adicionar widgets (elementos da interface)
tk.Label(janela, text="Nome do sabor").grid(row=0, column=0)
tk.Label(janela, text="Lucro por unidade").grid(row=0, column=1)
tk.Label(janela, text="Quantidade de leite por picolé").grid(row=0, column=2)
tk.Label(janela, text="Estoque de leite").grid(row=0, column=3)
tk.Label(janela, text="Quantidade de açúcar por picolé").grid(row=0, column=4)
tk.Label(janela, text="Estoque de açúcar").grid(row=0, column=5)
tk.Label(janela, text="Quantidade de polpa por picolé").grid(row=0, column=6)
tk.Label(janela, text="Estoque de polpa").grid(row=0, column=7)

entrada_sabor_x1 = tk.Entry(janela)
entrada_sabor_x2 = tk.Entry(janela)
entrada_sabor_x3 = tk.Entry(janela)
entrada_sabor_x4 = tk.Entry(janela)
entrada_sabor_x5 = tk.Entry(janela)
entrada_sabor_x1.grid(row=1, column=0)
entrada_sabor_x2.grid(row=2, column=0)
entrada_sabor_x3.grid(row=3, column=0)
entrada_sabor_x4.grid(row=4, column=0)
entrada_sabor_x5.grid(row=5, column=0)

entrada_lucro_x1 = tk.Entry(janela)
entrada_lucro_x2 = tk.Entry(janela)
entrada_lucro_x3 = tk.Entry(janela)
entrada_lucro_x4 = tk.Entry(janela)
entrada_lucro_x5 = tk.Entry(janela)
entrada_lucro_x1.grid(row=1, column=1)
entrada_lucro_x2.grid(row=2, column=1)
entrada_lucro_x3.grid(row=3, column=1)
entrada_lucro_x4.grid(row=4, column=1)
entrada_lucro_x5.grid(row=5, column=1)

entrada_leite_x1 = tk.Entry(janela)
entrada_leite_x2 = tk.Entry(janela)
entrada_leite_x3 = tk.Entry(janela)
entrada_leite_x4 = tk.Entry(janela)
entrada_leite_x5 = tk.Entry(janela)
entrada_leite_x1.grid(row=1, column=2)
entrada_leite_x2.grid(row=2, column=2)
entrada_leite_x3.grid(row=3, column=2)
entrada_leite_x4.grid(row=4, column=2)
entrada_leite_x5.grid(row=5, column=2)

entrada_max_leite = tk.Entry(janela)
entrada_max_leite.grid(row=3, column=3)

entrada_acucar_x1 = tk.Entry(janela)
entrada_acucar_x2 = tk.Entry(janela)
entrada_acucar_x3 = tk.Entry(janela)
entrada_acucar_x4 = tk.Entry(janela)
entrada_acucar_x5 = tk.Entry(janela)
entrada_acucar_x1.grid(row=1, column=4)
entrada_acucar_x2.grid(row=2, column=4)
entrada_acucar_x3.grid(row=3, column=4)
entrada_acucar_x4.grid(row=4, column=4)
entrada_acucar_x5.grid(row=5, column=4)

entrada_max_acucar = tk.Entry(janela)
entrada_max_acucar.grid(row=3, column=5)

entrada_polpa_x1 = tk.Entry(janela)
entrada_polpa_x2 = tk.Entry(janela)
entrada_polpa_x3 = tk.Entry(janela)
entrada_polpa_x4 = tk.Entry(janela)
entrada_polpa_x5 = tk.Entry(janela)
entrada_polpa_x1.grid(row=1, column=6)
entrada_polpa_x2.grid(row=2, column=6)
entrada_polpa_x3.grid(row=3, column=6)
entrada_polpa_x4.grid(row=4, column=6)
entrada_polpa_x5.grid(row=5, column=6)

entrada_max_polpa = tk.Entry(janela)
entrada_max_polpa.grid(row=3, column=7)

# Botão para resolver o problema
botao_resolver = tk.Button(janela, text="Resolver", command=resolver_problema)
botao_resolver.grid(row=7, column=0, columnspan=8)

# Resultado
resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=8, column=4, columnspan=8)

# Imagem
imagem_picole = PhotoImage(file="logo_picole.gif")
# Criar um Label para a imagem
imagem_label = tk.Label(janela, image=imagem_picole)
imagem_label.grid(row=9, column=0, columnspan=3)      
        


# Iniciar a execução da interface
janela.mainloop()

