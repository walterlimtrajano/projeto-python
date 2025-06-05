tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

def alternar_jogador():
    global jogador_atual
    jogador_atual = "O" if jogador_atual == "X" else "X"

def verificar_vitoria():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return True
    return False

def verificar_empate():
    for linha in tabuleiro:
        for celula in linha:
            if celula == "":
                return False
    return True

def clicar_linha_coluna(linha, coluna, botoes, label_status, mostrar_vitoria):
    if tabuleiro[linha][coluna] == "":
        tabuleiro[linha][coluna] = jogador_atual
        botoes[linha][coluna].config(text=jogador_atual, state="disabled")

        if verificar_vitoria():
            mostrar_vitoria(jogador_atual)
        elif verificar_empate():
            mostrar_vitoria("Empate")
        else:
            alternar_jogador()
            label_status.config(text=f"Vez do jogador: {jogador_atual}")
