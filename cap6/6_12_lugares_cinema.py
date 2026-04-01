lugares_vagos = [10, 2, 1, 3, 0]
ingressos_vendidos = [0, 0, 0, 0, 0]

while True:
    
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala invalida")
    elif lugares_vagos[sala -1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala -1]} vagos):"))
        if lugares > lugares_vagos[sala -1]:
            print("Esse numero de lugares não esta disponivel.")
        elif lugares < 0:
            print("Numero Invalido")
        else:
            lugares_vagos[sala -1] -= lugares
            ingressos_vendidos[sala -1] += lugares
            print(f"{lugares} lugares vendidos")
    print("Utilização das salas")
    for sala, vagos in enumerate(lugares_vagos):
        print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s), {ingressos_vendidos[sala]} ingresso(s) vendido(s)")
