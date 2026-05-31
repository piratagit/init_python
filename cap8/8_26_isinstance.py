def imprime_listas(lista, espaço, nivel=0):
    for x in lista:
        if isinstance(x, int):
            if espaço == "":
                print(f"{x:{nivel * 2}}")
            else:
                print(f"{nivel * espaço}{x}")
        else:
            imprime_listas(x, espaço, nivel + 1)

imprime_listas([1, [2, 3, 4], [5, 6, [7, 8]]], "--", 4)
