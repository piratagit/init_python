with open("pares.txt","w")as pares, open("impares.txt","w") as impares:
    with open("numeros.txt", "r") as numeros:
        for n in numeros.readlines():
            if int(n) % 2 == 0:
                pares.write(n)
            else:
                impares.write(n)
