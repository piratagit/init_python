def primos(maximo):
    primos = [2]
    num = 2
    while True:
        if num > maximo:
            print(primos)
            break
        else:
            num += 1
            print(f"num: {num}")
            for n in range(1, num):
                n += 1
                if n == num:
                    primos.append(num)
                if num % n == 0:
                    break

primos(15)
