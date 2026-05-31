import random

n = random.randint(1, 10)

for x in range(3):

    y = int(input("Escolha um número de 1 a 10: "))

    if y == n:
        print("Acertou")
        break

    if x == 2:
        print("Errou! Acabaram as tentativas!")

    else:
        print(f"Errou, tem mais {2 - x} chances !")

