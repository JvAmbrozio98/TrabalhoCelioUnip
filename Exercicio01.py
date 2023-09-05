

def imprimirNumerosAnterioresPosteriores():
    numero = int(input("Digite o numero desejado"))
    numerosAnteriores = []
    numerosPosteriores = []

    i = numero - 50
    while i < numero:
        numerosAnteriores.append(i)
        i += 1
       

    i = numero + 1
    while i < numero + 51:
        numerosPosteriores.append(i)
        i += 1

    print(f'\n Os numeros anteriores sao:{numerosAnteriores} \n')
    print(f'O numero digitado foi: {numero} \n')
    print(f'Os numeros posteriores sao:{numerosPosteriores} \n')


