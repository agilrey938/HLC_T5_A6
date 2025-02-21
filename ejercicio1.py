def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

entrada = [1, 2, 3, 4, 5, 6]
salida = suma_pares(entrada)
print(salida)