with open ("numeros.txt","w") as numeros:
    for n in range(0, 1000):
        numeros.write(f"{n}\n")
print('foi')
