casa = int(input("Qual o valor da casa? "))
salario = int(input("Qual o seu salario? "))
anos = int(input("Em quantos anos pretente pagar? "))

prestacao = casa/(anos * 12)

if prestacao > salario * 0.3:
    print(f"Emprestimo não aprovado, valor da prestação R$ {prestacao}")

else:
    print(f"Emprestimo aprovado, valor da prestação R$ {prestacao}")
