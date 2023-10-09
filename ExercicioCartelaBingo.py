import random

def gerar_cartela():
    cartela = []
    for i in range(5):
        coluna = random.sample(range(i * 15 + 1, i * 15 + 16), 5)
        cartela.extend(coluna)
    return cartela

def imprimir_cartela(cartela, nome):
    print(f"{'-' * 60}")
    print(f"|{' '}B   |  I   |  N   |  G   |  O   |{' '*11}|")
    print(f"{'-' * 60}")
    for i in range(5):
        for j in range(5):
            if j == 2 and i == 2:
                print(f"|  {nome}  |", end=" ")
            elif cartela[i * 5 + j] < 10:
                print(f"|  {cartela[i * 5 + j]}  |", end=" ")
            else:
                print(f"|  {cartela[i * 5 + j]} |", end=" ")
        print()
        print(f"{'-' * 60}")
    print(f"\n{' ' * 11}Nome: {nome}")


nome = input("Digite seu nome: ")
cartela = gerar_cartela()
imprimir_cartela(cartela, nome)
