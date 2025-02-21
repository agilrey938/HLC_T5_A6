def decimal_a_romano(numero):
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ''
    for valor, romano in valores:
        while numero >= valor:
            resultado += romano
            numero -= valor
    return resultado

entrada = 9
salida = decimal_a_romano(entrada)
print(salida)