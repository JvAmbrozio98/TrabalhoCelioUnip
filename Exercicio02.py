import random
def maiorNumeroDecimal ():
    n1 = int(input("Digite o numero desejado"))
    n2 = int(input("Digite o numero desejado"))
    n3 = int(input("Digite o numero desejado"))
    if ((n1>n2) and (n2 > n3)):
        print(f'O maior numero eh {n1} ')
    else:
        if(n2 >n3) :
            print(f'O maior numero eh {n2} ')
        else:
            print(f'O maior numero eh {n3} ')
    print(n1,n2,n3)


