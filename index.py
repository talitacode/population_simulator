import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# Função para simular o crescimento populacional
def simular_crescimento(populacao_inicial, taxa_crescimento, anos, pct_feminino, pct_criancas):
    dados = {'Ano': [], 'Masculino': [], 'Feminino': [], 'Crianças': []}
    
    populacao_total = populacao_inicial
    for ano in range(anos + 1):
        populacao_feminino = populacao_total * pct_feminino
        populacao_masculino = populacao_total - populacao_feminino
        populacao_criancas = populacao_total * pct_criancas
        
        # Armazenar os dados
        dados['Ano'].append(ano)
        dados['Masculino'].append(populacao_masculino - populacao_criancas/2)  # metade das crianças são masculinas
        dados['Feminino'].append(populacao_feminino - populacao_criancas/2)  # metade das crianças são femininas
        dados['Crianças'].append(populacao_criancas)

        # Atualizar a população total para o próximo ano
        populacao_total += populacao_total * taxa_crescimento
    
    return pd.DataFrame(dados)
def criar_interface_personalizada():
    root = tk.Tk()
    root.geometry("350x350")  # Definir tamanho da janela principal
    root.title("Crescimento Populacional")

    # Variáveis
    variaveis = {}

   # Função para criar a interface e coletar os parâmetros
    def pegar_valores():
        variaveis['populacao_inicial'] = int(entry_populacao.get())
        variaveis['taxa_crescimento'] = float(entry_taxa.get())
        variaveis['anos'] = int(entry_anos.get())
        variaveis['pct_feminino'] = float(entry_feminino.get())
        variaveis['pct_criancas'] = float(entry_criancas.get())
        root.quit()  # Fecha a janela

    # Labels e Entradas
    tk.Label(root, text="População Inicial: exemplo: 10000 ", anchor='w').pack(fill='x', padx=20, pady=5) 
    entry_populacao = tk.Entry(root)
    entry_populacao.pack(padx=20, pady=5) 

    tk.Label(root, text="Taxa de Crescimento:(decimal, exemplo: 0.02 para 2%):", anchor='w').pack(fill='x', padx=20, pady=5) 
    entry_taxa = tk.Entry(root)
    entry_taxa.pack(padx=20, pady=5) 

    tk.Label(root, text="Número de Anos:", anchor='w').pack(fill='x', padx=20, pady=5) 
    entry_anos = tk.Entry(root)
    entry_anos.pack(padx=20, pady=5) 

    tk.Label(root, text="Porcentagem Feminina:(decimal, exemplo: 0.5 para 50%):", anchor='w').pack(fill='x', padx=20, pady=5) 
    entry_feminino = tk.Entry(root)
    entry_feminino.pack(padx=20, pady=5) 

    tk.Label(root, text="Porcentagem de Crianças:(decimal, exemplo: 0.2 para 20%):", anchor='w').pack(fill='x', padx=20, pady=5) 
    entry_criancas = tk.Entry(root)
    entry_criancas.pack(padx=20, pady=5) 

    # Botão para capturar os valores
    tk.Button(root, text="Enviar", command=pegar_valores).pack()

    root.mainloop()  # Exibe a janela

    return variaveis['populacao_inicial'], variaveis['taxa_crescimento'], variaveis['anos'], variaveis['pct_feminino'], variaveis['pct_criancas']


# def criar_interface():
#     root = tk.Tk()
#     root.withdraw()  # Ocultar a janela principal
#     width = 200
#     height = 100
#     dialog.geometry(f"{width}x{height}")
#     populacao_inicial = int(simpledialog.askstring("Crescimento populacional", "Digite a população inicial:"))
#     taxa_crescimento = float(simpledialog.askstring("Crescimento populacional", "Digite a taxa de crescimento anual (em decimal, por exemplo, 0.02 para 2%):"))
#     anos = int(simpledialog.askstring("Crescimento populacional", "Digite o número de anos para simulação:"))
#     pct_feminino = float(simpledialog.askstring("Crescimento populacional", "Digite a porcentagem de população feminina (em decimal, por exemplo, 0.5 para 50%):"))
#     pct_criancas = float(simpledialog.askstring("Crescimento populacional", "Digite a porcentagem de crianças (em decimal, por exemplo, 0.2 para 20%):"))

#     return populacao_inicial, taxa_crescimento, anos, pct_feminino, pct_criancas

# Função para gerar o gráfico
def gerar_grafico(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Ano'], df['Masculino'], label='Masculino', marker='o')
    plt.plot(df['Ano'], df['Feminino'], label='Feminino', marker='o')
    plt.plot(df['Ano'], df['Crianças'], label='Crianças', marker='o')

    plt.title('Crescimento Populacional por Grupo')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.legend()
    plt.grid(True)
    plt.show()

# Execução do código
if __name__ == "__main__":
    # Coletar os parâmetros
    populacao_inicial, taxa_crescimento, anos, pct_feminino, pct_criancas = criar_interface_personalizada()

    # Simular o crescimento populacional
    df_crescimento = simular_crescimento(populacao_inicial, taxa_crescimento, anos, pct_feminino, pct_criancas)

    # Gerar o gráfico
    gerar_grafico(df_crescimento)
