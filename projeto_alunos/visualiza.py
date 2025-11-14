import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys
import subprocess


# --- Função para ler os dados do arquivo gerado pelo C ---
def ler_dados(arquivo):
    alunos = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                if not linha.strip():
                    continue
                nome, np1, np2, pim = linha.strip().split(",")
                np1, np2, pim = float(np1), float(np2), float(pim)
                media = (np1 + np2 + pim) / 3
                status = "Aprovado" if media >= 7 else "Reprovado"
                alunos.append((nome, np1, np2, pim, media, status))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'dados.txt' não encontrado. Execute primeiro o programa em C.")
    return alunos


# --- Função para exibir os dados na interface ---
def mostrar_alunos():
    for widget in container.winfo_children():
        widget.destroy()

    alunos = ler_dados("dados.txt")

    if not alunos:
        aviso = ttk.Label(container, text="Nenhum dado encontrado.", font=("Arial", 11))
        aviso.pack(pady=10)
        return

    for aluno in alunos:
        frame = ttk.Frame(container, padding=10)
        frame.pack(fill="x", padx=10, pady=5)

        nome_lbl = ttk.Label(frame, text=f"Aluno: {aluno[0]}", font=("Arial", 12, "bold"))
        nome_lbl.pack(anchor="w")

        notas_lbl = ttk.Label(
            frame,
            text=f"NP1: {aluno[1]:.1f} | NP2: {aluno[2]:.1f} | PIM: {aluno[3]:.1f} | Média: {aluno[4]:.1f}"
        )
        notas_lbl.pack(anchor="w")

        status_lbl = ttk.Label(
            frame,
            text=f"{aluno[5]}",
            foreground="green" if aluno[5] == "Aprovado" else "red",
            font=("Arial", 10, "bold")
        )
        status_lbl.pack(anchor="w")

    # Atualiza gráfico
    mostrar_grafico(alunos)


# --- Gráfico de barras das médias ---
def mostrar_grafico(alunos):
    for widget in grafico_frame.winfo_children():
        widget.destroy()

    nomes = [a[0] for a in alunos]
    medias = [a[4] for a in alunos]
    cores = ["green" if a[5] == "Aprovado" else "red" for a in alunos]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(nomes, medias, color=cores)
    ax.set_xlabel("Média Final")
    ax.set_title("Desempenho dos Alunos")
    ax.set_xlim(0, 10)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# --- Abrir o arquivo dados.txt no Bloco de Notas ---
def abrir_arquivo():
    caminho = os.path.abspath("dados.txt")
    if not os.path.exists(caminho):
        messagebox.showwarning("Aviso", "Arquivo 'dados.txt' não encontrado.")
        return

    try:
        if sys.platform.startswith("win"):  # Windows
            os.startfile(caminho)
        elif sys.platform == "darwin":  # macOS
            subprocess.call(["open", caminho])
        else:  # Linux
            subprocess.call(["xdg-open", caminho])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{e}")


# --- Interface Tkinter ---
janela = tk.Tk()
janela.title("Resultado dos Alunos (dados do programa em C)")
janela.geometry("700x600")
janela.minsize(600, 500)

titulo = ttk.Label(janela, text="Resultado dos Alunos", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Container com scrollbar
canvas = tk.Canvas(janela)
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
container = ttk.Frame(canvas)

container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=container, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Botões de controle
botoes_frame = ttk.Frame(janela)
botoes_frame.pack(pady=10)

btn_atualizar = ttk.Button(botoes_frame, text="🔄 Atualizar Dados", command=mostrar_alunos)
btn_atualizar.grid(row=0, column=0, padx=5)

btn_abrir = ttk.Button(botoes_frame, text="📂 Abrir dados.txt", command=abrir_arquivo)
btn_abrir.grid(row=0, column=1, padx=5)

# Espaço para o gráfico
grafico_frame = ttk.Frame(janela, padding=10)
grafico_frame.pack(fill="both", expand=True, pady=10)

mostrar_alunos()
janela.mainloop()
