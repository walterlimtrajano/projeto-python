import tkinter as tk
from tkinter import messagebox

jogo = [["" for _ in range(3)] for _ in range(3)]
jogador_da_vez = "X"

def trocar_turno():
    global jogador_da_vez
    jogador_da_vez = "O" if jogador_da_vez == "X" else "X"

def verificar_vitoria():
    for i in range(3):
        if jogo[i][0] == jogo[i][1] == jogo[i][2] != "":
            return True
        if jogo[0][i] == jogo[1][i] == jogo[2][i] != "":
            return True
    if jogo[0][0] == jogo[1][1] == jogo[2][2] != "":
        return True
    if jogo[0][2] == jogo[1][1] == jogo[2][0] != "":
        return True
    return False

def verificar_empate():
    for linha in jogo:
        for celula in linha:
            if celula == "":
                return False
    return True

def exibir_resultado(resultado):
    if resultado == "Empate":
        messagebox.showinfo("Resultado", "O jogo empatou!")
    else:
        messagebox.showinfo("Resultado", f"Jogador {resultado} venceu!")

    for i in range(3):
        for j in range(3):
            botoes[i][j].config(state="disabled")
    label_status.config(text="Fim de jogo")

def clicar_linha_coluna(linha, coluna):
    if jogo[linha][coluna] == "":
        jogo[linha][coluna] = jogador_da_vez
        cor = "blue" if jogador_da_vez == "X" else "red"
        botoes[linha][coluna].config(text=jogador_da_vez, state="disabled", fg=cor)

        if verificar_vitoria():
            exibir_resultado(jogador_da_vez)
        elif verificar_empate():
            exibir_resultado("Empate")
        else:
            trocar_turno()
            label_status.config(text=f"Vez do jogador: {jogador_da_vez}")

def resetar_jogo():
    global jogo, jogador_da_vez
    jogo = [["" for _ in range(3)] for _ in range(3)]
    jogador_da_vez = "X"
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal", fg="black")
    label_status.config(text="Vez do jogador: X")

janela = tk.Tk()
janela.title("Jogo da Velha")

botoes = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(janela, text="", font=("Arial", 24), width=5, height=2,
                                 command=lambda linha=i, coluna=j: clicar_linha_coluna(linha, coluna))
        botoes[i][j].grid(row=i, column=j)

label_status = tk.Label(janela, text="Vez do jogador: X", font=("Arial", 14))
label_status.grid(row=3, column=0, columnspan=3)

botao_resetar = tk.Button(janela, text="Novo Jogo", font=("Arial", 12), command=resetar_jogo)
botao_resetar.grid(row=4, column=0, columnspan=3, pady=10)

janela.mainloop()
