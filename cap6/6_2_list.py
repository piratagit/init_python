
l1 = []

l2 = []

x = 0

while x < 5:
    l1 += [int(input(f"Digite o {x + 1}° elemento da 1° lista: "))]
    x += 1

x = 0

while x < 5:
    l2 += [int(input(f"Digite o {x + 1}° elemento da 2° lista: "))]
    x += 1

l3 = l1 + l2

print(l3)
