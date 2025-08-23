
deposito = int(input("Digite o deposito inicial: "))

taxa = float(input("Digite a taxa de juros: "))

x = 1

total = deposito

total_taxa = 0

while x < 25:
    total_taxa = total_taxa + (total * taxa)
    print(f"{x}° mes - Total:{total:.2f} - Taxa:{total_taxa:.2f}")
    total = deposito + total_taxa
    x += 1
