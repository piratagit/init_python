
valor = int(input("Digite o valor a receber: "))

cedula = 100

resto = valor

while resto > 0:
    if resto > 99:
        notas = valor//cedula
        print(f"{notas} notas de {cedula}")
        resto = valor - (notas * cedula)
    elif resto > 49:
        cedula = 50
        notas = resto//cedula
        print(f"{notas} notas de {cedula}")
        resto = resto - (notas * cedula)
    elif resto > 19:
        cedula = 20
        notas = resto//cedula
        print(f"{notas} notas de {cedula}")
        resto = resto - (notas * cedula)
    elif resto > 9:
        cedula = 10
        notas = resto//cedula
        print(f"{notas} notas de {cedula}")
        resto = resto - (notas * cedula)
    elif resto > 4:
        cedula = 5
        notas = resto//cedula
        print(f"{notas} notas de {cedula}")
        resto = resto - (notas * cedula)
    elif resto > 0:
        cedula = 1
        notas = resto//cedula
        print(f"{notas} notas de {cedula}")
        resto = resto - (notas * cedula)
