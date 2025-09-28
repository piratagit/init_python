
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"\nFila atual: {fila}")
    print("Digite 'F' para adicionar um cliente no fim da fila, ")
    print("ou 'A' para realizar o atendimento. 'S' para sair.")
    operação = input("Operação (F, A ou S):")
    if operação == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia, ninguem para atender.")
    elif operação == 'F':
        ultimo += 1
        fila.append(ultimo)
        print(f"Adicionado o {ultimo}° cliente.")
    elif operação == 'S':
        break
    else:
        print("Operação invalida, difite 'F', 'A' ou 'S'")
