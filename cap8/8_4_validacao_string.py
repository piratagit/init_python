def valida_string(string, minimo, maximo):
    if len(string) > maximo or len(string) < minimo:
        return False
    else:
        return True

print(valida_string('batatasss', 8, 10))
