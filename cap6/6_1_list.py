
notas = [0, 0, 0, 0, 0]

x = 0

soma = 0

while x < 5:
    nota = float(input(f"Digite a {x+1}° nota: "))
    notas[x] = nota
    x += 1

x = 0

while x < 5:
    soma += notas[x]
    x += 1

print(f"A média é {soma/x:.2f}")
