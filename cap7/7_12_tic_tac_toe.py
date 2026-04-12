tab = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]
usados = []
fim = False

while True:

    print("\nDigite 0 para sair\n\n")

    while True:
        player1 = input("Jogador 1 joga, qual posiçao(como no teclado numérico)?\n")
        if player1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]:
            print("Posição invalida!")
            continue
        if player1 in usados:
            print("Posição ja ocupada!")
            continue
        usados += player1
        player1 = int(player1)
        x = int((player1-1)/3)
        # print(f"x = {x}")
        y = int(player1-(x*3)-1)
        # print(f"y = {y}")
        tab[x][y] = "X"
        break

    if player1 == 0:
        break

    for n in range(3):
        if tab[n] == ["X", "X", "X"]:
            print("Jogador 1 ganhou!")
            fim = True
            break

    if fim:
        break

    if (tab[0][0] == "X" and tab[1][1] == "X" and tab[2][2] == "X") or (tab[0][2] == "X" and tab[1][1] == "X" and tab[2][0] == "X"):
        print("Jogador 1 ganhou!")
        break
    elif (tab[0][0] == "X" and tab[1][0] == "X" and tab[2][0] == "X") or (tab[0][1] == "X" and tab[1][1] == "X" and tab[2][1] == "X") or (tab[0][2] == "X" and tab[1][2] == "X" and tab[2][2] == "X"):
        print("Jogador 1 ganhou!")
        break

    while True:
        player2 = input("Jogador 2 joga, qual posiçao(como no teclado numérico)?\n")
        if player2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]:
            print("Posição invalida!")
            continue
        if player2 in usados:
            print("Posição ja ocupada!")
            continue
        usados += player2
        player2 = int(player2)
        x = int((player2-1)/3)
        # print(f"x = {x}")
        y = int(player2-(x*3)-1)
        # print(f"y = {y}")
        tab[x][y] = "0"
        for n in range(3):
            print("-|---|----|----|-\n",tab[2-n])
        print("-|---|----|----|-\n")
        break

    if player2 == 0:
        break

    for n in range(3):
        if tab[n] == ["0", "0", "0"]:
            print("Jogador 2 ganhou!")
            fim = True
            break

    if fim:
        break

    if (tab[0][0] == "0" and tab[1][1] == "0" and tab[2][2] == "0") or (tab[0][2] == "0" and tab[1][1] == "0" and tab[2][0] == "0"):
        print("Jogador 2 ganhou!")
        break
    elif (tab[0][0] == "0" and tab[1][0] == "0" and tab[2][0] == "0") or (tab[0][1] == "0" and tab[1][1] == "0" and tab[2][1] == "0") or (tab[0][2] == "0" and tab[1][2] == "0" and tab[2][2] == "0"):
        print("Jogador 2 ganhou!")
        break
