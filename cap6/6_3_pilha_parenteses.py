
string = input("Escreva a expressão: ")

par_aberto = []

for char in string:
    if char == '(':
        par_aberto.append(char)
    elif char == ')':
        par_aberto.pop(-1)

print(f'Sobraram {len(par_aberto)} parenteses abertos na expressão')
