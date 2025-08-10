velocidade = int(input("Digite a velocidade: "))

if velocidade > 80:
    restante = velocidade - 80
    multa = restante * 5
    print(f"Voce foi multado em R${multa} reais!")
