import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

ARQUIVO_TAREFAS = "tarefas.json"

# ---------------- Persistência ----------------
def carregar_dados():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"ativas": [], "concluidas": []}

def salvar_dados():
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# ---------------- Lógica ----------------
def adicionar_tarefa():
    titulo = entrada_titulo.get()
    data_limite = entrada_data.get()
    prioridade = combo_prioridade.get()

    if not titulo or not data_limite or not prioridade:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        datetime.strptime(data_limite, "%d/%m/%Y")  # valida formato da data
    except ValueError:
        messagebox.showerror("Erro", "Data inválida! Use o formato DD/MM/AAAA.")
        return

    dados["ativas"].append({
        "titulo": titulo,
        "data": data_limite,
        "prioridade": prioridade
    })
    salvar_dados()
    atualizar_listas()
    entrada_titulo.delete(0, tk.END)
    entrada_data.delete(0, tk.END)

def concluir_tarefa():
    item = lista_ativas.selection()
    if not item:
        messagebox.showinfo("Info", "Selecione uma tarefa para concluir.")
        return
    index = lista_ativas.index(item)
    tarefa = tarefas_ordenadas[index]
    dados["ativas"].remove(tarefa)
    dados["concluidas"].append(tarefa)
    salvar_dados()
    atualizar_listas()

def atualizar_listas():
    global tarefas_ordenadas
    lista_ativas.delete(*lista_ativas.get_children())
    lista_concluidas.delete(*lista_concluidas.get_children())

    # Ordenar tarefas por prioridade + data
    tarefas_ordenadas = sorted(
        dados["ativas"],
        key=lambda t: (
            {"Alta": 1, "Média": 2, "Baixa": 3}[t["prioridade"]],
            datetime.strptime(t["data"], "%d/%m/%Y")
        )
    )
    hoje = datetime.today()

    # Ativas
    for t in tarefas_ordenadas:
        data_obj = datetime.strptime(t["data"], "%d/%m/%Y")
        atrasada = data_obj < hoje
        cor = "red" if atrasada else "black"
        lista_ativas.insert("", "end", values=(t["titulo"], t["data"], t["prioridade"]), tags=(cor,))

    # Concluídas
    for t in dados["concluidas"]:
        lista_concluidas.insert("", "end", values=(t["titulo"], t["data"], t["prioridade"]))

# ---------------- Interface Tkinter ----------------
janela = tk.Tk()
janela.title("📌 Minhas Tarefas")
janela.geometry("600x500")

# Inputs
frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Título:").grid(row=0, column=0, sticky="e")
entrada_titulo = tk.Entry(frame_inputs, width=40)
entrada_titulo.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Data limite (DD/MM/AAAA):").grid(row=1, column=0, sticky="e")
entrada_data = tk.Entry(frame_inputs, width=20)
entrada_data.grid(row=1, column=1, padx=5, sticky="w")

tk.Label(frame_inputs, text="Prioridade:").grid(row=2, column=0, sticky="e")
combo_prioridade = ttk.Combobox(frame_inputs, values=["Alta", "Média", "Baixa"], width=17)
combo_prioridade.grid(row=2, column=1, padx=5, sticky="w")

tk.Button(frame_inputs, text="Adicionar Tarefa", command=adicionar_tarefa).grid(row=3, column=1, pady=5, sticky="w")

# Lista de tarefas ativas
tk.Label(janela, text="Tarefas Ativas", font=("Arial", 12, "bold")).pack(pady=5)
colunas = ("Título", "Data Limite", "Prioridade")
lista_ativas = ttk.Treeview(janela, columns=colunas, show="headings", height=8)
for col in colunas:
    lista_ativas.heading(col, text=col)
lista_ativas.pack(expand=True, fill="both")
lista_ativas.tag_configure("red", foreground="red")

tk.Button(janela, text="✅ Concluir Selecionada", command=concluir_tarefa).pack(pady=5)

# Lista de tarefas concluídas
tk.Label(janela, text="Histórico de Concluídas", font=("Arial", 12, "bold")).pack(pady=5)
lista_concluidas = ttk.Treeview(janela, columns=colunas, show="headings", height=5)
for col in colunas:
    lista_concluidas.heading(col, text=col)
lista_concluidas.pack(expand=True, fill="both")

# Carregar dados
dados = carregar_dados()
tarefas_ordenadas = []
atualizar_listas()

janela.mainloop()
