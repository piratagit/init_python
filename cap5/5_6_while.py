stop = 0

num = 10000000000

while stop != 1:
    num += 1
    if num % 2 != 0:
        raiz = int(num ** (1/2)+1)
        while num % raiz != 0:
            raiz -= 1
            if raiz == 1:
                stop = int(input(f"{num} é primo! Deseja continuar? "))
