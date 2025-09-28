
ultimo = 10
continua = True
fila = list(range(1, ultimo + 1))
while continua:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"\nFila atual: {fila}")
    print("Digite 'F' para adicionar um cliente no fim da fila, ")
    print("ou 'A' para realizar o atendimento. 'S' para sair.")
    operação = list(input("Operação (F, A ou S):"))
    print(operação)

    for op in operação:
        if op == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia, ninguem para atender.")
        elif op == 'F':
            ultimo += 1
            fila.append(ultimo)
            print(f"Adicionado o {ultimo}° cliente.")

        elif op == 'S':
            continua = False
        else:
            print("Operação invalida, difite 'F', 'A' ou 'S'")
